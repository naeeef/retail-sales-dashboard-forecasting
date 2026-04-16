# Retail Sales Dashboard & Forecasting

Transforms raw retail sales data into actionable insights and revenue forecasts using Python and Power BI.

---

## Business Problem

Retail businesses generate large volumes of sales data but often lack clear visibility into:
- Which categories drive the majority of revenue
- How sales performance changes over time
- What future demand will look like

This project addresses these gaps through structured data analysis and forecasting.

---

## Overview

This project processes raw retail sales data, performs exploratory data analysis, and builds a forecasting model to predict future sales trends. The results are presented through an interactive Power BI dashboard for decision-making.

---

## Impact

Enables identification of key revenue drivers and supports data-driven business decisions through trend analysis and forecasting.

---

## Dataset

- Retail sales dataset containing transaction-level data
- Includes date, category, quantity, price, and total sales
- Aggregated to monthly level for trend and forecasting analysis

---

## Dashboard

<img width="1528" height="880" alt="dashboard png" src="https://github.com/user-attachments/assets/b162e5eb-40f5-49c8-90e1-f2c775f3062b" />

---

## Key Insights

- Revenue exhibits seasonal volatility with a mid-year decline followed by Q4 recovery
- Revenue distribution is concentrated in a few categories, indicating dependency risk
- Growth trend strengthens toward year-end, suggesting demand acceleration
- Forecast projects continued upward momentum in the short term

---

## Skills Demonstrated

- Data Cleaning & Transformation (Pandas)
- Exploratory Data Analysis (EDA)
- Time-based Aggregation and Trend Analysis
- Forecasting using Linear Regression
- Data Visualization & Storytelling (Power BI)
- Data Pipeline Development (Python → Power BI)

---

## Tech Stack

- Python (Pandas, NumPy, Scikit-learn)
- Power BI
- CSV (Data Storage)

---

## Workflow

1. Load and parse raw transaction data (`retail_sales.csv`)
2. Clean and validate date fields; handle missing values
3. Aggregate sales by month and category
4. Apply linear regression to model sales trend over time
5. Forecast next 6 months; clip predictions within realistic bounds
6. Export structured outputs for Power BI ingestion
7. Visualize actuals vs. forecast in an interactive dashboard

---

## Outputs Generated

| File | Description |
|---|---|
| `monthly_sales.csv` | Month-by-month revenue aggregation |
| `category_revenue.csv` | Revenue ranked by category |
| `forecast.csv` | 6-month forward sales forecast |
| `combined_sales.csv` | Actuals + forecast merged for visualization |

---

## Project Structure

```
retail-sales-dashboard-forecasting/
│
├── data/
│   └── retail_sales.csv
│
├── outputs/
│   ├── category_revenue.csv
│   ├── monthly_sales.csv
│   ├── forecast.csv
│   └── combined_sales.csv
│
├── images/
│   └── dashboard.png
│
├── dashboard.pbix
├── analysis.py
├── requirements.txt
└── README.md
```

---

## How to Run

```bash
pip install -r requirements.txt
python analysis.py
```

Outputs will be saved to the `outputs/` folder and can be connected directly to `dashboard.pbix` in Power BI.

---

## Outcome

- Transformed raw transaction data into structured, analysis-ready datasets
- Identified key revenue drivers and seasonal patterns across categories
- Built a regression-based forecasting model with bounded predictions
- Delivered an interactive dashboard to support data-driven decisions

---

## Limitations

- Forecast is based on linear regression — a trend-only model
- Does not capture seasonality, promotions, or external market factors
- Accuracy improves with longer historical data

---

## Future Improvements

- Implement time-series models (ARIMA, Prophet) for seasonality handling
- Add automated data pipeline for real-time updates
- Expand dashboard filtering by region, product, and time period

---

## Author

Mohammed Naef Nazar
