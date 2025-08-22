import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet
from prophet.plot import plot_plotly

# Title and description
st.title("Reliance Stock Price Forecast")
st.markdown("This app performs time series forecasting on Reliance stock prices using Facebook Prophet.")

# Load and preprocess data
@st.cache_data
def load_data():
    df = pd.read_csv("C:/Users/abhis/OneDrive/Desktop/stock time series/RELIANCE.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[['Date', 'Close']].rename(columns={"Date": "ds", "Close": "y"})
    return df

data = load_data()

# Show raw data
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data.tail())

# Plot historical closing price
st.subheader("Historical Closing Price")
st.line_chart(data.set_index("ds"))

# Forecast horizon
periods_input = st.slider('How many days would you like to forecast into the future?', min_value=3, max_value=365, value=90)

# Forecasting
model = Prophet()
model.fit(data)
future = model.make_future_dataframe(periods=periods_input)
forecast = model.predict(future)

# Forecast plot
st.subheader("Forecasted Data")
st.plotly_chart(plot_plotly(model, forecast))

# Forecast components
st.subheader("Forecast Components")
components_fig = model.plot_components(forecast)
st.write(components_fig)

# Future 3-day prediction
st.subheader("Next 3 Days Forecast")
next_3_days = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods_input).head(3)
st.write(next_3_days)

# Download link
csv = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(index=False)
st.download_button("Download Forecast Data", csv, "forecast.csv", "text/csv")
