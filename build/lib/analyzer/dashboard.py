import streamlit as st
import pandas as pd
import re
import json

def load_data(path="report/suspicious_activity.json"):
    with open(path) as f:
        return pd.DataFrame(json.load(f))

st.set_page_config(page_title="SSH Attack Analyzer", layout="wide")

st.title("🚨 SSH Attack Dashboard")
df = load_data()

def extract_log_date(timestamp):
    match = re.match(r"^\w+\s+\d+", str(timestamp))
    return match.group(0) if match else "Unknown"

df["log_date"] = df["timestamp"].apply(extract_log_date)

st.sidebar.header("🔍 Filters")
all_dates = sorted(df["log_date"].dropna().unique())
selected_dates = st.sidebar.multiselect("Select Dates", all_dates, default=all_dates)
filtered_df = df[df["log_date"].isin(selected_dates)]

if filtered_df.empty:
    st.warning("⚠ No entries match the selected date(s). Try adjusting your filter.")

st.subheader("Summary Stats")
st.metric("Total Failed Attempts", len(filtered_df))
st.metric("Unique IPs", filtered_df["ip"].nunique())
st.metric("Top Attacker", filtered_df["ip"].value_counts().idxmax())

st.subheader("Top 10 Attacking IPs")
top_ips = filtered_df["ip"].value_counts().head(10)
st.bar_chart(top_ips)

st.subheader("Top 10 Targeted Usernames")
top_users = filtered_df["username"].value_counts().head(10)
st.bar_chart(top_users)

with st.expander("📄 Raw Data Table"):
    st.dataframe(filtered_df)
