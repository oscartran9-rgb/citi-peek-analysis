
# Citibike Demand Analysis & Dynamic Pricing Recommendation

## Overview

This project explores New York City’s Citibike trip data to uncover demand patterns and develop pricing strategies. The analysis is designed to support business decisions for Peek’s travel app by forecasting ridership trends and identifying opportunities to optimize pricing and service offerings.

---

## 🧠 Methodology

- Conducted **exploratory data analysis (EDA)** using SQL to understand temporal demand and assess the structure of available data.
- Applied both **SARIMAX** and **ETS (Exponential Smoothing)** models to evaluate short-term and seasonal forecasting performance.
- Focused analysis on **rider type**, particularly *customers*, to shape targeted recommendations for app-based pricing.
- Addressed **data limitations** (e.g., missing boroughs, time gaps from Sept 2016–Mar 2017) by supplementing with external data sources for improved completeness.

---

## 🛠️ Tools & Libraries Used

### Tools
- **Jupyter Notebook** – For iterative analysis and prototyping
- **BigQuery** – To efficiently query large-scale Citibike datasets
- **Streamlit** – For rapid visualization and prototyping of the dynamic pricing model

### Python Libraries

- `os` – Operating system interfaces  
- `pandas` – Data manipulation and analysis  
- `sqlite3` – Lightweight disk-based database support (optional for local prototyping)  
- `google.cloud.bigquery` – Google BigQuery Python client for cloud data querying  
- `statsmodels.tsa.statespace.SARIMAX` – SARIMAX model for time series forecasting  
- `statsmodels.tsa.holtwinters.ExponentialSmoothing` – ETS model for trend/seasonality smoothing  
- `sklearn.metrics.mean_absolute_percentage_error` – For evaluating model accuracy  
- `matplotlib.pyplot` & `matplotlib.dates` – Plotting and date formatting for visualizations  
- `seaborn` – Statistical data visualization (used for heatmaps, optional)  
- `glob` – File pattern matching in directory trees  
- `pathlib.Path` – Object-oriented file system paths
- `streamlit` – For rapid visualization and prototyping of the dynamic pricing model

---

## 📊 Key Findings

- **Seasonal Trends**: Summer months (May–September) consistently show the highest ridership. Winter months (December–February) experience significant dips due to colder weather.
- **Hourly Patterns**: High-frequency trip periods align with peak commute hours, indicating strong weekday commuter behavior.
- **Customer Behavior**: Customer rides often begin and end at the same station (e.g., *Central Park S & 6th Ave*), suggesting they’re more likely using bikes for leisure or loop trips.

---

## 💰 Pricing Recommendations

- **Dynamic Pricing**: Increase weekday rates during peak commute hours, especially in the summer, to maximize revenue.
- **Incentives for Off-Peak Travel**: Offer discounts during winter and late evening hours to increase ridership.
- **Leisure-Based Promotions**: Highlight popular round-trip locations (e.g., Central Park) in tourist-focused pricing bundles.
- **Event & Weather Integration**: Incorporate real-time event and weather data into pricing strategy to better match short-term demand shifts.

---

*Built with curiosity, data, and bikes 🚲*
