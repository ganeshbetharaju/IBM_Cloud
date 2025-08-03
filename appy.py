import streamlit as st
import requests

# Replace with your real credentials from IBM Cloud
API_KEY = "YOUR_API_KEY"
PROJECT_ID = "YOUR_PROJECT_ID"
LOCATION = "us-south"  # Change if your region is different

def get_eco_suggestion(activity):
    url = f"https://{LOCATION}.ml.cloud.ibm.com/ml/v1/text/generate"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "project_id": PROJECT_ID,
        "input": f"Suggest an eco-friendly alternative to this activity: {activity}"
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json().get("results", [{}])[0].get("generated_text", "No suggestion found.")
    except Exception as e:
        return f"Error: {e}"

st.title("🌿 Eco Lifestyle Agent")
st.write("Track your daily activity and get eco-friendly suggestions.")

activity = st.text_input("Enter your activity (e.g. driving petrol car):")

if st.button("Get Suggestion"):
    if activity:
        suggestion = get_eco_suggestion(activity)
        st.success(suggestion)
    else:
        st.warning("Please enter an activity.")
