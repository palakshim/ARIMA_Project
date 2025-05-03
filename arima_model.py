import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

def load_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['Date'], index_col='Date')
    return df

def train_arima_model(series, order=(1,1,1)):
    model = ARIMA(series, order=order)
    model_fit = model.fit()
    return model_fit

def forecast(model_fit, steps=10):
    return model_fit.forecast(steps=steps)

