import streamlit as st
import pandas as pd # Pandas is a Python module that helps you work with data easily (It arranges data in a structured way using DataFrames (like rows & columns in Excel))
import datetime # For handling dates
import csv # For reading and writing CSV file
import os # For file operations (operating system)

MOOD_FILE = "mood_log.csv"

def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"]) # Creating two colomns to file
    return pd.read_csv(MOOD_FILE)

def save_mood_data(date, mood):
    file_exists = os.path.exists(MOOD_FILE)
    with open(MOOD_FILE, "a") as file: # 'a' stands for append 
        if not file_exists:
            writer.writerow(["Date", "Mood"])
        writer = csv.writer(file)
        writer.writerow([date, mood]) # Write data in row form 

# Streamlit app title
st.title("Mood Tracker")
st.subheader("How are your feeling today?")
mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

today = datetime.date.today()

if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success("Mood Logged Successfully!")

# Load existing mood data
data = load_mood_data()

# If there is data to display
if not data.empty:
    st.subheader("Mood Trends Over Time")

    data["Date"] = pd.to_datetime(data["Date"])
    mood_counts = data["Mood"].value_counts()
    
    st.bar_chart(mood_counts)

    st.write("Build with ❤️ by [Muhamamd Arsalan Khan](https://github.com/ar813)")

    