import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 

import pickle
with open('model (3).pkl', 'rb') as file:
    model = pickle.load(file)

# Now you can use 'model' in your app



# Get feature names (e.g., you have these stored in a list)
feature_names = ['tenure', 'monthly_charges', 'total_charges', 'contract', 'paperless_billing', 
                 'payment_method', 'senior_citizen', 'gender', 'partner', 'dependents', 'phone_service', 
                 'multiple_lines', 'internet_service', 'online_security', 'online_backup', 
                 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies']

# Create a DataFrame for easy plotting
importances =  ['Tenure', 'Monthly Charges', 'Total Charges', 'Contract Type', 'Paperless Billing', 
            'Payment Method', 'Senior Citizen', 'Gender', 'Partner', 'Dependents', 
            'Phone Service', 'Multiple Lines', 'Internet Service', 'Online Security', 
            'Online Backup', 'Device Protection', 'Tech Support', 'Streaming TV', 
            'Streaming Movies']
feature_importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importances
})

# Sort by importance
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

# Plot the feature importance
plt.figure(figsize=(10,6))
sns.barplot(x='Importance', y='Feature', data=feature_importance_df)
plt.title('Feature Importance for Churn Prediction')
plt.show()
