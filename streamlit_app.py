import numpy as np
import pickle
import streamlit as st
import os

# Get the correct file path of the trained model
model_path = os.path.join(os.path.dirname(__file__), "trained_model.sav")

# Load the model
with open(model_path, "rb") as file:
    loaded_model = pickle.load(file)

# Creating a function for Prediction
def diabetes_prediction(input_data):
    # Changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data, dtype=np.float64)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'

def main():
    # Giving a title
    st.title('Diabetes Prediction Web App')

    # Getting the input data from user
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    Age = st.text_input('Age of the Person')

    # Code for Prediction
    diagnosis = ''

    # Creating a button for Prediction
    if st.button('Diabetes Test Result'):
        try:
            # Convert inputs to float
            input_data = [
                float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)
            ]
            diagnosis = diabetes_prediction(input_data)
        except ValueError:
            diagnosis = "Please enter valid numeric values."

    st.success(diagnosis)

if __name__ == '__main__':
    main()
   
