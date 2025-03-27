import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_excel("classified_clinical_trials.xlsx")

# Title
st.title("Clinical Trials Dashboard")

# Sidebar
st.sidebar.header("Filters")
selected_phase = st.sidebar.multiselect("Select Phase", df["Phases"].unique())

# Filter Data
if selected_phase:
    df = df[df["Phases"].isin(selected_phase)]

# Visualizations
st.subheader("Distribution of Clinical Trials by Phase")
fig, ax = plt.subplots()
df["Phases"].value_counts().plot(kind="bar", ax=ax)
st.pyplot(fig)

st.subheader("Number of Trials per Location")
fig, ax = plt.subplots()
df["LocationCountry"].value_counts().plot(kind="bar", ax=ax)
st.pyplot(fig)

st.subheader("Classification Results for Study Titles")
fig, ax = plt.subplots()
df["Category"].value_counts().plot(kind="bar", ax=ax)
st.pyplot(fig)

st.dataframe(df)  # Show Data
