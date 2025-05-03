import streamlit as st
from arima_model import load_data, train_arima_model, forecast
import matplotlib.pyplot as plt

st.title("ARIMA Forecasting App")

uploaded_file = st.file_uploader("Upload a CSV with Date and Value columns")

if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.write("Uploaded Data", df.head())
    
    if st.button("Train Model and Forecast"):
        model_fit = train_arima_model(df['Value'])
        future = forecast(model_fit, steps=10)
        
        st.write("Forecasted Values", future)
        plt.figure(figsize=(10,5))
        plt.plot(df.index, df['Value'], label='Original')
        plt.plot(future.index, future, label='Forecast', linestyle='--')
        plt.legend()
        st.pyplot(plt)
