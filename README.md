# 📈 ARIMA Time Series Forecasting Web App

This project is an interactive web application built using **Streamlit** to perform **time series forecasting** with the **ARIMA (AutoRegressive Integrated Moving Average)** model. It allows users to upload their own time series datasets (e.g., stock prices, weather data, etc.), train a forecasting model, and visualize predictions—all through a clean browser interface.

---

## 📚 What is ARIMA?

ARIMA stands for:
- **AR (AutoRegressive)**: Uses past values to predict future values.
- **I (Integrated)**: Differencing raw observations to make the data stationary.
- **MA (Moving Average)**: Uses past forecast errors in a regression-like model.

This model is well-suited for univariate time series data that shows trends over time.

---

## 🔍 Key Features

- Upload custom time series datasets (CSV)
- Automatically convert and parse datetime formats
- Train and apply ARIMA models to make forecasts
- View plots of actual vs. predicted values
- Simple and fast Streamlit-based user interface

---

## 🚀 How to Use

1. Upload a CSV file with two columns: `Date` and `Value`.
2. The app preprocesses and fits the ARIMA model on your data.
3. Forecasts are generated for a user-defined number of future time steps.
4. Visualizations display both actual and predicted values.

**Example Input:**
```csv
Date,Value
2023-01-01,120
2023-01-02,125
...


