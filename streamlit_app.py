pip install streamlit pandas matplotlib

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- App title ---
st.title("NBA Data Explorer (Past 15 Seasons)")

# --- Load CSV ---
try:
    df = pd.read_csv('tbt.csv')
except FileNotFoundError:
    st.error("CSV file not found! Make sure 'tbt.csv' is in the same folder.")
    st.stop()

# --- Sidebar filters ---
st.sidebar.header("Filters")
season = st.sidebar.selectbox("Select Season:", sorted(df['Season'].unique(), reverse=True))
teams_in_season = df[df['Season'] == season]['Team'].unique()
team = st.sidebar.selectbox("Select Team:", sorted(teams_in_season))

# --- Filtered Data ---
filtered_data = df[(df['Season'] == season) & (df['Team'] == team)]

st.subheader(f"Data for {team} in {season}")
st.dataframe(filtered_data)

# --- Show correlation matrix ---
if st.sidebar.checkbox("Show correlations"):
    st.subheader("Correlation Matrix")
    st.write(filtered_data.corr())

# --- Plot a numeric stat ---
numeric_columns = filtered_data.select_dtypes(include=['int64', 'float64']).columns.tolist()

if numeric_columns:
    stat_to_plot = st.sidebar.selectbox("Select stat to plot:", numeric_columns)
    st.subheader(f"{stat_to_plot} Plot")
    
    # Simple bar chart
    fig, ax = plt.subplots()
    ax.bar(filtered_data.index, filtered_data[stat_to_plot])
    ax.set_xlabel("Index")
    ax.set_ylabel(stat_to_plot)
    st.pyplot(fig)
else:
    st.info("No numeric columns to plot in this filtered data.")

