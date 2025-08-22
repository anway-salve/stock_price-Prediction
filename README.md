# 📈 Reliance Stock Price Forecasting App  

This project is a **time series forecasting application** built with **Streamlit** that predicts **Reliance stock prices** using **Facebook Prophet**. It allows users to explore historical stock prices, generate future forecasts, visualize trends, and download forecast data.  

---

## ⚡ Features  

- 📊 **View Historical Stock Prices** – Interactive line chart of past closing prices.  
- 🔮 **Forecast Future Prices** – Predict stock prices for the next **3–365 days**.  
- 🧩 **Trend Analysis** – Visualize forecast components (trend, weekly & yearly seasonality).  
- 📅 **Next 3-Day Forecast** – Quick insight into upcoming stock price predictions.  
- 💾 **Download Forecast Data** – Export predictions as a CSV file.  

---

## 📂 Project Structure  

```
├── reliance_forecast.py     # Streamlit app code
├── RELIANCE.csv             # Dataset (historical Reliance stock prices)
```

---

## ⚙️ Requirements  

Install dependencies:  

```bash
pip install streamlit pandas plotly prophet
```

⚠️ **Note:**  
- For Prophet, you may need additional libraries (like `pystan` or `cmdstanpy`).  
- Recommended:  
  ```bash
  pip install prophet
  ```

---

## 🚀 Running the App  

Run the Streamlit app:  

```bash
streamlit run reliance_forecast.py
```

Then open the link in your browser (default: `http://localhost:8501/`).  

---

## 📊 Dataset  

The dataset used is **`RELIANCE.csv`**, which should include at least:  

- `Date` – Trading date (format: YYYY-MM-DD)  
- `Close` – Closing stock price  

Example:  

| Date       | Close   |  
|------------|---------|  
| 2024-01-01 | 2480.50 |  
| 2024-01-02 | 2495.80 |  

---

## 🔮 Model  

- Uses **Facebook Prophet** for time series forecasting.  
- Input: `Date` (as `ds`), `Close` price (as `y`).  
- Output:  
  - `yhat` – Predicted stock price  
  - `yhat_lower` – Lower bound of prediction  
  - `yhat_upper` – Upper bound of prediction  

---

## 📌 Notes  

- Place `RELIANCE.csv` in the same directory as the script.  
- You can adjust forecast horizon with the slider (3–365 days).  
- Forecast graphs are interactive (zoom, pan, hover).  

---

✅ This app helps investors, analysts, and researchers explore **future stock trends** with intuitive visualizations.  
