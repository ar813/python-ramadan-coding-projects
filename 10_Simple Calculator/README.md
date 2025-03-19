# Simple Calculator

A simple web-based calculator built using [Streamlit](https://streamlit.io/). This calculator allows users to perform basic arithmetic operations (Addition, Subtraction, Multiplication, and Division) between two numbers.

## Features

- User-friendly interface with number inputs
- Supports four basic operations: Addition, Subtraction, Multiplication, and Division
- Displays results dynamically with clear formatting
- Error handling for division by zero

## Installation

Ensure you have Python installed (preferably Python 3.7 or later). Then, install the required dependencies:

```sh
uv init .
uv add streamlit pandas
```

## Usage

Activate the virtual environment and run the script using the following commands:

```sh
.venv\Scripts\activate
streamlit run main.py
```

## How It Works

1. Enter two numbers in the provided input fields.
2. Select the desired arithmetic operation.
3. Click the "Calculate" button to view the result.
4. If division by zero occurs, an error message is displayed.

## Example

If you input:

- **First Number**: `10`
- **Second Number**: `5`
- **Operation**: `Multiplication (×)`

The output will be:

```
10 × 5 = 50
```

## Author

Developed by Muhammad Arsalan Khan.

