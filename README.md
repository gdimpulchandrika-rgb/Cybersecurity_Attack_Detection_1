### Cybersecurity Intrusion Detection System

## Project Overview
This project builds a Machine Learning–based Intrusion Detection System (IDS) to identify whether a network session is normal or a potential cyber attack.

Cyber attacks are increasing rapidly, and organizations need automated systems to detect suspicious behavior.
This project uses machine learning algorithms to analyze network activity and predict possible attacks.

The final model is deployed as an interactive web application using Streamlit and Hugging Face Spaces.

## Problem Statement

Traditional security systems rely on rule-based detection, which cannot detect new or unknown attacks.

The goal of this project is to:

* Analyze cybersecurity session data
* Train a machine learning model to detect attacks
* Build a user interface where users can input session details
* Predict whether the activity is Normal or an Attack

## Dataset
The dataset contains information about network sessions and user behavior.
Example Features:
* Session Duration
* Encryption Used
* IP Reputation Score
* Failed Login Attempts
* Browser Type
* Unusual Time Access
* Network Protocol
* Request Frequency

## Target Variable
* attack_detected
0 → Normal activity
1 → Attack detected
  

Project Structure
Cybersecurity-Attack-Detection
│
├── 01_EDA.ipynb          # Data cleaning and Exploratory Data Analysis
├── 02_Modeling.ipynb     # Machine learning model training
├── app.py                # Streamlit web application
├── best_model.pkl        # Saved trained model
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

## Exploratory Data Analysis (EDA)
In the EDA phase:
* Checked dataset structure
* Handled missing values
* Performed feature analysis
* Studied relationships between variables
* Identified patterns in attack vs normal activity

Libraries used:

!.Pandas
2.Matplotlib
3.Seaborn
4.Model Building
5.Multiple machine learning models were tested.

Example models:
1.Logistic Regression
2.Decision Tree
3.Random Forest

## Final Selected Model
RandomForestClassifier

## Reason for selection:
* High accuracy
* Handles complex patterns
* Robust against overfitting

## Model Saving

* The trained model was saved using Pickle.
 
"import pickle
pickle.dump(model, open("best_model.pkl", "wb"))"

This allows the model to be reused in the web application.

## Web Application (Streamlit)

A Streamlit interface was created where users can input session details.

Example inputs:
* Session Duration
* Encryption Type
* IP Reputation Score
* Failed Login Attempts
* Browser Type
* Unusual Time Access
The model predicts whether the activity is:
* Normal
* Attack Detected

## Deployment
The application is deployed using Hugging Face Spaces.
Huggong face web application Link: https://huggingface.co/spaces/DIMPULCHANDRIKA19/cybersecurity-attack-detection-1

## To run the project locally:
Step 1: Clone the repository
git clone https://github.com/yourusername/cybersecurity-attack-detection.git

Step 2: Navigate to the project folder
cd cybersecurity-attack-detection

Step 3: Install requirements
pip install -r requirements.txt

Step 4: Run the Streamlit app
streamlit run app.py

## Technologies Used:
* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Hugging Face Spaces
* Matplotlib
* Seaborn

## Future Improvements
Add more cybersecurity datasets
Improve model accuracy with deep learning
Add real-time network monitoring
Deploy using Docker and cloud services

## Author
Dimpul Chandrika Gudapati
Kavya Madala

## Machine Learning Project
Cybersecurity Attack Detection System
