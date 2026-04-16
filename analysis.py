import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "retail_sales.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUT_PATH, exist_ok=True)


def load_data():
    df = pd.read_csv(DATA_PATH)
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
    return df


def category_analysis(df):
    category_revenue = (
        df.groupby("Category")["Total_Sales"]
        .sum()
        .reset_index()
        .sort_values(by="Total_Sales", ascending=False)
    )
    category_revenue.to_csv(os.path.join(OUTPUT_PATH, "category_revenue.csv"), index=False)


def monthly_analysis(df):
    df["Month"] = df["Date"].dt.to_period("M")
    monthly_sales = df.groupby("Month")["Total_Sales"].sum().reset_index()
    monthly_sales["Month"] = monthly_sales["Month"].dt.to_timestamp()

    monthly_sales.to_csv(os.path.join(OUTPUT_PATH, "monthly_sales.csv"), index=False)
    return monthly_sales


def forecasting(monthly_sales):
    monthly_sales["Time_Index"] = np.arange(len(monthly_sales))

    X = monthly_sales[["Time_Index"]]
    y = monthly_sales["Total_Sales"]

    model = LinearRegression()
    model.fit(X, y)

    future_index = np.arange(len(monthly_sales), len(monthly_sales) + 6)
    forecast_values = model.predict(future_index.reshape(-1, 1))

    last_value = y.iloc[-1]
    forecast_values = np.clip(forecast_values, last_value * 0.8, last_value * 1.2)

    future_dates = pd.date_range(
        start=monthly_sales["Month"].iloc[-1],
        periods=7,
        freq="ME"
    )[1:]

    forecast_df = pd.DataFrame({
        "Month": future_dates,
        "Forecast_Sales": forecast_values
    })

    forecast_df.to_csv(os.path.join(OUTPUT_PATH, "forecast.csv"), index=False)
    return forecast_df


def create_combined(monthly_sales, forecast_df):
    monthly_sales["Type"] = "Actual"
    forecast_df["Type"] = "Forecast"

    last_row = monthly_sales.iloc[[-1]].copy()
    last_row = last_row.rename(columns={"Total_Sales": "Sales"})
    last_row["Type"] = "Forecast"

    monthly_sales_renamed = monthly_sales.rename(columns={"Total_Sales": "Sales"})
    forecast_df_renamed = forecast_df.rename(columns={"Forecast_Sales": "Sales"})

    forecast_df_renamed = pd.concat([last_row, forecast_df_renamed])

    combined = pd.concat([monthly_sales_renamed, forecast_df_renamed])
    combined = combined.sort_values(by="Month")

    combined = combined.drop(columns=["Time_Index"], errors="ignore")
    combined = combined.dropna()

    combined.to_csv(os.path.join(OUTPUT_PATH, "combined_sales.csv"), index=False)


def main():
    df = load_data()
    category_analysis(df)
    monthly_sales = monthly_analysis(df)
    forecast_df = forecasting(monthly_sales)
    create_combined(monthly_sales, forecast_df)


if __name__ == "__main__":
    main()