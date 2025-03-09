# The Simple APIs

## Overview

The Simple APIs is a simple web application built with FastAPI. It gives users random side hustle ideas and money quotes. You need an API key to use it.

## Features

- **Get Side Hustle Ideas**: Get a random idea for a side job to earn extra money.
- **Get Money Quotes**: Get an inspiring quote about money and finance.

## Technologies Used

- **Python** (FastAPI framework)
- **Random Module** (For selecting random results)

## How to Install

1. Initialize the virtual environment and install FastAPI:
   ```bash
   uv init .
   uv add fastapi[standard]
   ```
2. Activate the virtual environment:
   ```bash
   .venv\Scripts\activate  # On Windows
   ```
3. Start the application:
   ```bash
   fastapi dev main.py
   ```

## API Endpoints

### 1. Get a Random Side Hustle Idea

- **URL:** `/side_hustles`
- **Method:** `GET`
- **Query Parameter:** `api_key` (Required)
- **Example Response:**
  ```json
  {
      "side_hustle": "Freelancing - Start offering your skills online!"
  }
  ```
- **Test it in browser:** [http://127.0.0.1:8000/side\_hustles?api\_key=1234567890](http://127.0.0.1:8000/side_hustles?api_key=1234567890)

### 2. Get a Random Money Quote

- **URL:** `/money_quotes`
- **Method:** `GET`
- **Query Parameter:** `api_key` (Required)
- **Example Response:**
  ```json
  {
      "money_quote": "Money is a terrible master but an excellent servant. – P.T. Barnum"
  }
  ```

## API Key Authentication

To use the API, you must include an API key in the request. The default key is `1234567890`. If you do not provide a key or use the wrong one, you will get an error.

## Testing the API

- **Access the endpoints directly:**
  - [http://127.0.0.1:8000/side\_hustles](http://127.0.0.1:8000/side_hustles)
  - [http://127.0.0.1:8000/money\_quotes](http://127.0.0.1:8000/money_quotes)
- **Use Swagger UI for testing:**
  - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Contributing

If you want to improve this project, feel free to share your ideas or fix issues!

## Contact

For any questions, email [ar3584158@gmail.com](mailto\:ar3584158@gmail.com).

