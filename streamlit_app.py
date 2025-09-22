import streamlit as st
import pandas as pd

# --- App title ---
st.title("NBA Data Explorer (Past 15 Seasons)")

# --- Load CSV ---
try:
    df = pd.read_csv('tbt.csv')  # Make sure tbt.csv is in the same repo/folder
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

# --- Optional correlation matrix ---
if st.sidebar.checkbox("Show correlations"):
    st.subheader("Correlation Matrix")
    st.write(filtered_data.corr())


