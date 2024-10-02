import streamlit as st

def main():
    st.title("Churn Prediction")

    st.write("### Please provide the following details:")

    # Ensure each input is properly defined and placed
    senior_citizen = st.selectbox("Is the customer a senior citizen?", ['Yes', 'No'])
    gender = st.selectbox("Gender", ['Male', 'Female'])
    partner = st.selectbox("Has a partner", ['Yes', 'No'])
    dependents = st.selectbox("Has dependents", ['Yes', 'No'])
    phone_service = st.selectbox("Has phone service", ['Yes', 'No'])
    multiple_lines = st.selectbox("Multiple Lines", ['Yes', 'No', 'No phone service'])
    internet_service = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
    online_security = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
    online_backup = st.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])
    device_protection = st.selectbox("Device Protection", ['Yes', 'No', 'No internet service'])
    tech_support = st.selectbox("Tech Support", ['Yes', 'No', 'No internet service'])
    streaming_tv = st.selectbox("Streaming TV", ['Yes', 'No', 'No internet service'])
    streaming_movies = st.selectbox("Streaming Movies", ['Yes', 'No', 'No internet service'])

    # You can display these values to debug if needed
    st.write(f"Senior Citizen: {senior_citizen}")
    st.write(f"Gender: {gender}")
    st.write(f"Partner: {partner}")
    st.write(f"Dependents: {dependents}")
    st.write(f"Phone Service: {phone_service}")
    st.write(f"Multiple Lines: {multiple_lines}")
    st.write(f"Internet Service: {internet_service}")
    st.write(f"Online Security: {online_security}")
    st.write(f"Online Backup: {online_backup}")
    st.write(f"Device Protection: {device_protection}")
    st.write(f"Tech Support: {tech_support}")
    st.write(f"Streaming TV: {streaming_tv}")
    st.write(f"Streaming Movies: {streaming_movies}")

if __name__ == "__main__":
    main()
