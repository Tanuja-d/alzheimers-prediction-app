import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('alzheimers_model.pkl')

# Function to make predictions
def predict(input_data):
    # Convert the input data into a DataFrame
    input_df = pd.DataFrame([input_data], columns=input_data.keys())
    # Predict using the loaded model
    prediction = model.predict(input_df)
    return prediction

# Streamlit interface
st.title('Alzheimer\'s Disease Prediction')

st.write("""
    This app predicts the presence of Alzheimer’s disease based on input features.
    Enter the values for the features below and click on "Predict" to get the result.
""")

# Create input fields for the user
input_data = {
    'FunctionalAssessment': st.number_input('FunctionalAssessment', min_value=0.0, max_value=100.0, step=0.1),
    'ADL': st.number_input('ADL', min_value=0.0, max_value=100.0, step=0.1),
    'MMSE': st.number_input('MMSE', min_value=0.0, max_value=100.0, step=0.1),
    'MemoryComplaints': st.number_input('MemoryComplaints', min_value=0.0, max_value=100.0, step=0.1),
    # Add other features similarly
}

# When the user clicks "Predict"
if st.button('Predict'):
    prediction = predict(input_data)
    #st.write(f'Prediction: {prediction[0]}')
    st.write("Prediction:", "Alzheimer's" if prediction[0] == 1 else "No Alzheimer's")
