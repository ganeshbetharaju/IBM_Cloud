import streamlit as st
import requests

# Replace with your real credentials from IBM Cloud
API_KEY = "s1Y9Hu761s1NXyU7Qq_vclhQ23iD6mhV2uW1uXShT7Z1"
PROJECT_ID = "fa380080-64a3-412f-94e5-2e7e8aa78e12"
LOCATION = "us-south" 

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
