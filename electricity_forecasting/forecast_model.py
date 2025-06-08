
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_consumption(csv_file, days_to_forecast=7):
    df = pd.read_csv(csv_file, parse_dates=['Date'])
    df['Days'] = (df['Date'] - df['Date'].min()).dt.days
    X = df[['Days']]
    y = df['Consumption_kWh']

    model = LinearRegression()
    model.fit(X, y)

    last_day = df['Days'].iloc[-1]
    future_days = np.arange(last_day + 1, last_day + 1 + days_to_forecast).reshape(-1, 1)
    predictions = model.predict(future_days)

    future_dates = [df['Date'].max() + pd.Timedelta(days=i) for i in range(1, days_to_forecast + 1)]
    forecast_df = pd.DataFrame({'Date': future_dates, 'Predicted_Consumption_kWh': predictions})
    return forecast_df
