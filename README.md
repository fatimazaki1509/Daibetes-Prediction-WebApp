🚀 Tech Stack
Machine Learning Model: Support Vector Classifier (SVC)

Framework: Streamlit (for UI)

Programming Language: Python


Libraries Used:

numpy, pandas (data handling)
scikit-learn (machine learning)
pickle (for model saving/loading)
streamlit (for web app development)

📊 Dataset:
The model was trained using the Pima Indians Diabetes Dataset from Kaggle. The dataset consists of 8 medical predictor variables and a binary outcome (0 = Not Diabetic, 1 = Diabetic).

Features used for prediction:

Pregnancies
Glucose Level
Blood Pressure
Skin Thickness
Insulin Level
BMI
Diabetes Pedigree Function
Age

🔥 How It Works
The user inputs their health parameters in the web form.
The SVC model processes the inputs and makes a prediction.
The result is displayed on the screen:
✅ The person is not diabetic (Green)
❌ The person is diabetic (Red)


📥 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/fatimazaki1509/diabetes-prediction-app.git
cd diabetes-prediction-app

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run diabetes_prediction_webapp.py![Screenshot 2025-03-03 004141](https://github.com/user-attachments/assets/922e92ca-bf95-4b0b-8e18-690a55fd9f13)

The app will open in your browser at localhost:8501.


🌍 **Live Demo:** [Diabetes Prediction App](https://daibetes-prediction-webapp-68lbodae6atfyrhkuobyn6.streamlit.app/)  
