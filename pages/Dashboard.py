import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
from PIL import Image
from datetime import datetime, date
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import pickle
with open('model (3).pkl', 'rb') as file:
    model = pickle.load(file)

# Now you can use 'model' in your app
# Setting page configuration
st.set_page_config(page_title="churn segmenation", page_icon="✈️", layout='wide')

# Loading data
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)



# Information Cards
card1, card2, card3, card4 = st.columns((2,2,2,4))

# Filtered DataFrame
#filtered_data = filter(airline, source, destination, add_info)

# Cards Values
flight_count = df['MultipleLines'].count()
highest_Price = df['TotalCharges'].max()
lowest_Price = df['TotalCharges'].min()
top_airline = df['MultipleLines'].value_counts().idxmax()
# Show The Cards
card1.metric("Flight Count", f"{flight_count}")
card2.metric("Highest Price", f"{highest_Price}")
card3.metric("Lowest Price", f"{lowest_Price}")
card4.metric("Top Airline", f"{top_airline}")

# Dashboard Tabs
tab1, tab2, tab3 = st.tabs(["🏠 Home", "📈 Insights", "🤖 Prediction"])
# introduction

