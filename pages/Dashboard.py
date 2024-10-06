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
#with open('model (3).pkl', 'rb') as file:
    #model = pickle.load(file)

# Now you can use 'model' in your app
# Setting page configuration
st.set_page_config(page_title="churn segmenation", page_icon="✈️", layout='wide')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Check if a file is uploaded
if uploaded_file is not None:
  
# Read the uploaded file into a DataFrame
  df = pd.read_csv(uploaded_file)

  
else:
    st.write("Please upload a CSV file.")
card1, card2, card3, card4 = st.columns((2,2,2,4))

st.write(df.columns)
# Filtered DataFrame
#filtered_data = filter(airline, source, destination, add_info)

# Cards Values

highest_TotalCharges = df['TotalCharges'].max()
lowest_TotalCharges = df['TotalCharges'].min()

# Show The Cards
card1.metric("highest_TotalCharges", f"{highest_TotalCharges}")
card2.metric("lowest_TotalCharges", f"{lowest_TotalCharges}")
#card3.metric("Lowest Price", f"{lowest_Price}")
#card4.metric("Top Airline", f"{top_airline}")

# Load the dataset


tab1, tab2, tab3 = st.tabs(["🏠 Home", "📈 Insights", "🤖 Prediction"])

# Introduction Section
with tab1:
   st.write("In today's competitive business landscape, customer churn is a critical metric. "
                 "Churn refers to the percentage of customers that stop using a service over a certain period. "
                 "By predicting churn, businesses can take action to retain customers and improve overall satisfaction.")
       
from PIL import Image
import os

try:
    image = Image.open('0_d58iZ6esNNcfntQ7.jpg')
except FileNotFoundError:
    print("Image file not found, please check the file path.")
   
    
  
with tab2:
    st.subheader('Key Metrics & Data Analysis')

    visual1, visual2 = st.columns((5, 5))
    with visual1:
        st.subheader('Churn Distribution')
        churn_counts = df['Churn'].value_counts()
        fig = px.pie(values=churn_counts.values, names=['No Churn', 'Churn'], hole=0.4)
        st.plotly_chart(fig, use_container_width=True)

    with visual2:
        st.subheader('Monthly Charges Distribution')
        fig = px.histogram(df, x='MonthlyCharges', nbins=50)
        st.plotly_chart(fig, use_container_width=True)

    st.subheader('Correlation Heatmap')
    fig = px.imshow(df[['tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']].corr(), color_continuous_scale='RdBu_r', 
                    title='Correlation Heatmap of Key Features')
    st.plotly_chart(fig, use_container_width=True)
    if input_data.ndim == 1:
    input_data = np.expand_dims(input_data, axis=0)  # Reshape to 2D

    # Now pass the input data to the model
    try:
        churn_prediction = model.predict(input_data)
    except ValueError as e:
        print(f"Error during prediction: {e}")
    st.write("### Key Insights:")
    st.write("""
    1. **Tenure**: Customers with longer tenure are less likely to churn.
    2. **Monthly Charges**: Higher monthly charges are associated with higher churn rates.
    3. **Total Charges**: Shows a moderate correlation with churn, but further analysis is needed.
    """)

# Prediction Model Section
with tab3:
    st.subheader('Predict Customer Churn')

    model = joblib.load('model (3).pkl')  # Load your pre-trained model
    sc = StandardScaler()

    col1, col2 = st.columns((5, 5))
    with col1:
        gender_pred = st.selectbox("Gender", ["Male", "Female"])
        gender_pred = 1 if gender_pred == "Male" else 0
        
        senior_pred = st.selectbox("Senior Citizen", [0, 1])
        partner_pred = st.selectbox("Partner", [0, 1])
        dependents_pred = st.selectbox("Dependents", [0, 1])
        tenure_pred = st.slider("Tenure (in months)", min_value=0, max_value=72, step=1)

    with col2:
        phone_service_pred = st.selectbox("Phone Service", [0, 1])
        internet_service_pred = st.selectbox("Internet Service", [0, 1, 2])  # Assuming encoded values
        online_security_pred = st.selectbox("Online Security", [0, 1])
        monthly_charges_pred = st.number_input("Monthly Charges", min_value=0.0)

    # Prepare input for model
    input_data = sc.fit_transform([[gender_pred, senior_pred, partner_pred, dependents_pred, tenure_pred, 
                                    phone_service_pred, internet_service_pred, online_security_pred, 
                                    monthly_charges_pred]])

    if st.button("Predict Churn"):
        churn_prediction = model.predict(input_data)
        st.metric("Churn Prediction", "Yes" if churn_prediction == 1 else "No")

