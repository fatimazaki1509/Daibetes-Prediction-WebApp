# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 23:46:27 2025

@author: FATIMA
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('C:/Users/FATIMA/Downloads/Deploy ML Model/trained_model.sav','rb'))

#creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return'The person is not diabetic'
    else:
      return'The person is diabetic'
      
      
def main():
    
    #giving a title
    st.title('Diabetes Prediction Web App')
    
    #getting the input data from user
    
    Pregnencies = st.text_input('Number of Pregnencies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    Age = st.text_input('Age of the Person')
    
    #code for Prediction 
    diagnosis = ''
    
    #creating a button for Prediction 
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnencies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
        
    st.success(diagnosis)
     
     
     
if __name__ == '__main__':

   main()     
    
    
    