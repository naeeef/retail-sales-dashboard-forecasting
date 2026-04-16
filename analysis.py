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


def pareto_analysis(df):
    customer_sales = (
        df.groupby("Customer_ID")["Total_Sales"]
        .sum()
        .reset_index()
        .sort_values(by="Total_Sales", ascending=False)
    )

    customer_sales["Cumulative"] = (
        customer_sales["Total_Sales"].cumsum()
        / customer_sales["Total_Sales"].sum()
    )

    customer_sales.to_csv(os.path.join(OUTPUT_PATH, "pareto_analysis.csv"), index=False)


def regression_model(df):
    X = df[["Quantity", "Price"]]
    y = df["Total_Sales"]

    model = LinearRegression()
    model.fit(X, y)

    metrics = pd.DataFrame({
        "Metric": ["R2 Score"],
        "Value": [model.score(X, y)]
    })

    metrics.to_csv(os.path.join(OUTPUT_PATH, "model_metrics.csv"), index=False)


def forecasting(monthly_sales):
    monthly_sales["Time_Index"] = np.arange(len(monthly_sales))

    X = monthly_sales[["Time_Index"]]
    y = monthly_sales["Total_Sales"]

    model = LinearRegression()
    model.fit(X, y)

    future_index = np.arange(len(monthly_sales), len(monthly_sales) + 6)
    forecast = model.predict(future_index.reshape(-1, 1))

    future_dates = pd.date_range(
        start=monthly_sales["Month"].iloc[-1],
        periods=7,
        freq="ME"
    )[1:]

    forecast_df = pd.DataFrame({
        "Month": future_dates,
        "Forecast_Sales": forecast
    })

    forecast_df.to_csv(os.path.join(OUTPUT_PATH, "forecast.csv"), index=False)


def main():
    df = load_data()
    category_analysis(df)
    monthly_sales = monthly_analysis(df)
    pareto_analysis(df)
    regression_model(df)
    forecasting(monthly_sales)


if __name__ == "__main__":
    main()