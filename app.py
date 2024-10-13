import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from utils import load_data, calculate_health_metrics

st.set_page_config(page_title="Community Health Dashboard", layout="wide")

# Title and Introduction
st.title("Community Health Analysis Dashboard 🏥")
st.markdown("""
This dashboard helps analyze health data for community well-being.  
You can explore trends, analyze vaccination status, hospital usage, and other metrics.
""")

# Sidebar for File Upload
st.sidebar.header("Upload Health Data")
uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

# Load Data
if uploaded_file is not None:
    data = load_data(uploaded_file)
    st.success("Data loaded successfully!")
else:
    st.info("Loading sample data...")
    data = load_data("data/sample_health_data.csv")

# Data Overview
st.subheader("Data Overview")
st.write(data.head())

# Health Metrics Section
st.subheader("Key Health Metrics")
metrics = calculate_health_metrics(data)
col1, col2, col3 = st.columns(3)
col1.metric("Total Cases", metrics['total_cases'])
col2.metric("Total Vaccinated", metrics['total_vaccinated'])
col3.metric("Hospital Occupancy", f"{metrics['hospital_occupancy']}%")

# Disease Distribution
st.subheader("Disease Distribution")
disease_fig = px.pie(data, names='Disease', title="Distribution of Diseases")
st.plotly_chart(disease_fig, use_container_width=True)

# Time Series Analysis: Cases Over Time
st.subheader("Cases Over Time")
fig, ax = plt.subplots()
data.groupby('Date')['Cases'].sum().plot(kind='line', ax=ax)
ax.set_title("Total Cases Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Number of Cases")
st.pyplot(fig)

# Hospital Capacity Analysis
st.subheader("Hospital Capacity Usage")
hospital_fig = px.bar(data, x='Hospital', y='Occupancy Rate', title="Hospital Capacity Usage")
st.plotly_chart(hospital_fig, use_container_width=True)

# Vaccination Progress
st.subheader("Vaccination Progress")
vaccination_fig = px.histogram(data, x='Vaccination Status', title="Vaccination Distribution")
st.plotly_chart(vaccination_fig, use_container_width=True)

st.markdown("---")
st.markdown("Made with ❤️ by your community health team.")
