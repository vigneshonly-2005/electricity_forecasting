
import pandas as pd
import matplotlib.pyplot as plt
from forecast_model import forecast_consumption

def plot_forecast(csv_file, days_to_forecast=7):
    df = pd.read_csv(csv_file, parse_dates=['Date'])
    forecast_df = forecast_consumption(csv_file, days_to_forecast)

    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Consumption_kWh'], label='Historical Consumption')
    plt.plot(forecast_df['Date'], forecast_df['Predicted_Consumption_kWh'], label='Forecasted Consumption', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Consumption (kWh)')
    plt.title('Electricity Consumption Forecast')
    plt.legend()
    plt.tight_layout()
    plt.show()
 
if __name__ == "__main__":
    plot_forecast("data/sample_consumption.csv", days_to_forecast=7)

