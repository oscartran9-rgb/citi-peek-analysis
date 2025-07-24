import pandas as pd
import numpy as np
import streamlit as st

# Simulate 100 sample trip conditions
np.random.seed(42)
df = pd.DataFrame({
    'demand': np.random.randint(0, 99, size=100),
    'supply': np.random.randint(1, 99, size=100),
    'hour': np.random.randint(0, 24, size=100),
    'month': np.random.randint(1, 12, size=100),
    'start_station': np.random.choice([
        "Pershing Square North", "E 17 St & Broadway", "W 21 St & 6 Ave",
        "8 Ave & W 31 St", "Lafayette St & E 8 St", "Broadway & E 22 St",
        "8 Ave & W 33 St", "W 41 St & 8 Ave", "W 38 St & 8 Ave",
        "W 31 St & 7 Ave", "Hs Don't Use", "WS Don't Use",
        "Expansion Warehouse 333 Johnson Ave", "Gowanus Tech Station",
        "Apache", "NYCBS Depot - FAR", "Expansion Tech Station",
        "LPI Facility", "2 Ave & E 105 St", "333 Johnson TEST 1"
    ], size=100),
    'rider_type': np.random.choice(['Subscriber', 'Customer'], size=100),
    'weather': np.random.choice(['Clear', 'Sunny', 'Windy', 'Rain', 'Snow'], size=100),
    'event_flag': np.random.choice([0, 1], size=100, p=[0.8, 0.2])
})

def dynamic_price(row):
    base = 5.0
    demand_supply_ratio = row['demand'] / max(row['supply'], 1)

    if demand_supply_ratio >= 0.8:
        base += 2.5
    elif demand_supply_ratio >= 0.66:
        base += 1.0
    elif demand_supply_ratio <= 0.33:
        base -= 0.5

    if 7 <= row['hour'] <= 9 or 16 <= row['hour'] <= 19:
        base += 1.0
    elif 0 <= row['hour'] <= 5 or 20 <= row['hour'] <= 23:
        base -= 0.5

    if 5 <= row['month'] <= 9:
        base += 1.0
    elif 1 <= row['month'] <= 2 or row['hour'] == 12:
        base -= 0.5

    if row['start_station'] in ['Pershing Square North', 'E 17 St & Broadway', 'W 21 St & 6 Ave', '8 Ave & W 31 St', 'Lafayette St & E 8 St']:
        base += 1.0
    elif row['start_station'] in ['NYCBS Depot - FAR', 'Expansion Tech Station', 'LPI Facility', '2 Ave & E 105 St', '333 Johnson TEST 1']:
        base -= 0.5

    if row['weather'] in ['Rain', 'Snow']:
        base -= 1.5
    if row['weather'] in ['Sunny']:
        base += 2.5
    if row['event_flag'] == 1:
        base += 1.5

    if row['rider_type'] == 'Customer':
        base += 20.0
    elif row['rider_type'] == 'Subscriber':
        base = 219.99

    return round(max(base, 1.0), 2)

st.title("🚲 Dynamic Pricing Model Simulator")

st.markdown("Adjust the inputs below to see how the dynamic pricing changes based on various contextual factors.")

demand = st.slider("Bike Checked Out (Demand)", 0, 99, 10)
supply = st.slider("Available Bikes (Supply)", 1, 99, 60)
hour = st.slider("Hour of Day", 0, 23, 8)
month = st.slider("Month", 1, 12, 5)
start_station = st.selectbox("Start Station", options=sorted(df['start_station'].unique()))
rider_type = st.selectbox("Rider Type", options=['Subscriber', 'Customer'])
weather = st.selectbox("Weather", options=['Clear', 'Sunny', 'Windy', 'Rain', 'Snow'])
event_flag = st.radio("Major Event?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

row = {
    'demand': demand,
    'supply': supply,
    'hour': hour,
    'month': month,
    'start_station': start_station,
    'rider_type': rider_type,
    'weather': weather,
    'event_flag': event_flag
}

price = dynamic_price(row)
st.success(f"💰 Suggested Price: ${price}")