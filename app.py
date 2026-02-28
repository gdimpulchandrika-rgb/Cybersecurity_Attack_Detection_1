import streamlit as st
import joblib
import pandas as pd

# ---------------------------
# Load Trained Model
# ---------------------------
model = joblib.load("best_model.pkl")

# ---------------------------
# App Title
# ---------------------------
st.title("🔐 Cybersecurity Attack Detection System")

st.write("Enter session details below to predict whether the activity is malicious or normal.")

# ---------------------------
# User Inputs
# ---------------------------

network_packet_size = st.number_input("Network Packet Size", min_value=0.0)

protocol_type = st.selectbox(
    "Protocol Type",
    ["TCP", "UDP", "ICMP"]
)

login_attempts = st.number_input("Login Attempts", min_value=0)

session_duration = st.number_input("Session Duration (seconds)", min_value=0.0)

encryption_used = st.selectbox(
    "Encryption Used",
    ["AES", "DES"]
)

ip_reputation_score = st.number_input("IP Reputation Score", min_value=0.0)

failed_logins = st.number_input("Failed Login Attempts", min_value=0)

browser_type = st.selectbox(
    "Browser Type",
    ["Chrome", "Firefox", "Edge", "Safari"]
)

unusual_time_access = st.selectbox(
    "Unusual Time Access",
    [0,1]
)

# ---------------------------
# Convert Input to DataFrame
# ---------------------------

input_data = pd.DataFrame([{
    "network_packet_size": network_packet_size,
    "protocol_type": protocol_type,
    "login_attempts": login_attempts,
    "session_duration": session_duration,
    "encryption_used": encryption_used,
    "ip_reputation_score": ip_reputation_score,
    "failed_logins": failed_logins,
    "browser_type": browser_type,
    "unusual_time_access": unusual_time_access
}])

# ---------------------------
# Prediction Button
# ---------------------------

if st.button("Predict"):

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("Attack Detected!")
    else:
        st.success("Normal Traffic")

    st.write(f"Attack Probability: {probability:.2%}")