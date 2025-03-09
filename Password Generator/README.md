# Password Generator

## Overview

This project is part of my **Python Ramadan Coding Projects** series and is project number 3.

The Password Generator is a simple web-based application built using Streamlit. It allows users to generate strong passwords based on user preferences, such as length, inclusion of numbers, and special characters.

## Features

- Generate random passwords with customizable length (6-32 characters)
- Option to include numbers (0-9)
- Option to include special characters (!@#\$%^&\*)
- Simple and interactive UI using Streamlit

## Requirements

To run the Password Generator, you need to have Python installed along with the required dependencies.

### Install Python Dependencies

Run the following commands to set up the environment and install dependencies using UV:

```sh
uv init .  # Initialize the UV virtual environment
uv add streamlit  # Install Streamlit using UV
```

## How to Run

1. Save the script as `password_generator.py`
2. Open a terminal and navigate to the script's directory.
3. Activate the virtual environment:

```sh
.venv\Scripts\activate  # Activate the virtual environment on Windows
```

4. Run the following command to start the application:

```sh
streamlit run password_generator.py
```

5. The application will open in your web browser, where you can set preferences and generate a password.

## Usage

- Adjust the password length using the slider.
- Check the boxes to include numbers and/or special characters.
- Click the **Generate Password** button to get a randomly generated password.
- The generated password will be displayed on the screen.

## Technologies Used

- **Python**: Core programming language
- **Streamlit**: For building the web-based UI
- **Random & String Modules**: To generate random passwords

## Author

Developed by Muhammad Arsalan Khan

