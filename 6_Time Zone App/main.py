import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
import time

TIME_ZONES = [
    "UTC", # UTC stands for Coordinated Universal Time (It is the world standard time) as PAT stands for Pakistan Standard Time
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

st.set_page_config(page_title="Time Zone Converter", page_icon="⏳", layout="centered")
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌍 Time Zone Converter ⏳</h1>", unsafe_allow_html=True)


selected_timezone = st.multiselect("Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

st.subheader("Selected Timezones")
for tz in selected_timezone: # tz = time zone
    current_time = datetime.now(ZoneInfo(tz)).strftime("📅 %d-%m-%Y | 🕒 %I:%M:%S %p") # %d = Day, %m = Month, %Y = Year, %I = Hour(12-hour format), %H = Hour(24-hour format), %M = Minutes, %S = Seconds, %p = AM/PM indicator
    st.write(f"**{tz}**: {current_time}")


st.subheader("🔄 Convert Time Between Timezones")
current_time = st.time_input("Current Time", value=datetime.now().time())
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

if st.button("🚀 Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz)) # datetime.combine(): Combines today's date with current_time to create a full datetime object
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d | 🕒 %I:%M:%S %p")
    st.success(f"✅ **Converted Time ({to_tz})**: `{converted_time}`")

st.markdown("<h6 style='text-align: center; color: #888;'>Developed with by Muhammad Arsalan Khan ❤️</h6>", unsafe_allow_html=True)

