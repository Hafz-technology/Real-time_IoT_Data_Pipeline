import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import time

st.set_page_config(page_title="IoT Smart Home Dashboard", layout="wide")
st.title("The Data Pioneers: IoT Smart Home Hub")


db_string = "postgresql://depi:123456@postgres:5432/iot_db"

db = create_engine(db_string)

if st.button('Refresh Data'):
    st.rerun()

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔌 Energy Monitoring")
    try:
        query = "SELECT * FROM historical_data WHERE sensor_type='Energy'"
        df_energy = pd.read_sql(query, db)
        st.line_chart(df_energy.set_index('timestamp')['value'])
        
        hogs = df_energy[df_energy['status'] == 'Energy Hog']
        if not hogs.empty:
            st.error(f"Detected {len(hogs)} High Energy Consumption Events!")
    except Exception as e:
        st.info("Waiting for Batch ETL data...")

with col2:
    st.subheader("🌡️ Environment & Security")
    try:
        query = "SELECT * FROM historical_data WHERE sensor_type='Environment'"
        df_env = pd.read_sql(query, db)
        st.area_chart(df_env.set_index('timestamp')['value'])
    except:
        st.info("Waiting for data...")

st.divider()

st.subheader("🚨 Real-time Security Alerts")
try:
    alerts = pd.read_sql("SELECT * FROM alerts ORDER BY timestamp DESC LIMIT 5", db)
    st.dataframe(alerts)
except:
    st.write("No alerts yet or Alert table not created")
    
    
    
    
    
    
