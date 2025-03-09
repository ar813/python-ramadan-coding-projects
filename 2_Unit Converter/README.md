# The Unit Converter

## Project Overview

Welcome to **Project 2: Unit Converter** in the **Python Ramadan Coding Projects 2025** series! 🌙✨ This project is a simple yet efficient unit converter built using **Python** and **Streamlit**. It allows users to convert between different measurement units such as length and mass in an interactive web-based interface.

## Features

- Convert units between:
  - **Meters ↔ Kilometers**
  - **Grams ↔ Kilograms**
- Interactive UI using **Streamlit**
- User-friendly input fields for selecting units
- Instant conversion results displayed on-screen

## Technologies Used

- **Python**
- **Streamlit** (for creating the web UI)

## Installation & Setup

To set up and run this project, follow these steps:

```sh
uv init
uv add streamlit
.venv\Scripts\activate
streamlit run <file_name>.py
```

### Explanation of Commands

- `uv init` initializes a new virtual environment for managing dependencies.
- `uv add streamlit` installs Streamlit within the virtual environment.
- `.venv\Scripts\activate` activates the virtual environment, ensuring all installed dependencies are available.
- `streamlit run <file_name>.py` runs the Streamlit application and opens it in the browser.

## How to Use

1. Run the application using Streamlit.
2. Enter a value in the input field.
3. Select the unit to convert **from** and **to**.
4. Click the **Convert** button.
5. View the converted result instantly!

## Code Explanation

This project consists of a **unit conversion function** and a **Streamlit-based UI**:

### Conversion Function

```python
# Function to convert units
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
    }
    key = f"{unit_from}_{unit_to}"
    return value * conversions[key] if key in conversions else "Conversion not supported"
```

- The function checks the conversion dictionary.
- If the conversion exists, it multiplies the value by the factor.
- If the conversion is not defined, it returns an error message.

### Streamlit UI

```python
import streamlit as st  # Import Streamlit for UI

st.title("Simple Unit Converter")

value = st.number_input("Enter value:", min_value=1.0, step=1.0)
unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted Value: {result}")
```

- The **UI** takes user input for value and unit selection.
- On clicking **Convert**, the result is displayed instantly.

## Acknowledgments

- **Sir Asharib Ali** for the **Ramadan Coding Nights Challenge** 🎯
- **Streamlit** for providing an amazing web-based UI framework 🚀

**Stay tuned for more projects in this series! Happy coding & Ramadan Mubarak! 🌙🤲**

