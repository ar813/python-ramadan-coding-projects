# Money Making Machine

This project is a simple **Streamlit** web application that generates random money, provides side hustle ideas, and shares money-related motivational quotes. **Side hustle ideas and money quotes depend on another project, 4_Simple APIs, which must be set up separately.** The application interacts with a FastAPI server to fetch side hustles and money quotes.

## Features

- **Instant Cash Generator**: Click a button to generate a random amount of money.
- **Side Hustle Ideas**: Get a random side hustle suggestion to earn extra income.
- **Money Quotes**: Get an inspiring money-related quote.

## Technologies Used

- Python
- Streamlit
- Random Module (for generating money amounts)
- Requests Module (for fetching API data)
- Time Module (for delay effects)

## Installation & Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/ar813/python-ramadan-coding-projects.git
   cd python-ramadan-coding-projects
   ```

2. Initialize and install dependencies using `Uv`:

   ```sh
   uv init .
   uv add streamlit requests
   ```

3. Activate the virtual environment:

   ```sh
   .venv\Scripts\activate  # On Windows
   ```

4. Run the Streamlit application:

   ```sh
   streamlit run app.py
   ```

## How It Works

1. **Instant Cash Generator**: Click the "Generate Money" button to receive a random amount.
2. **Side Hustle Ideas**: Click "Generate Hustle" to get a random side hustle idea.
3. **Money Quotes**: Click "Get Inspired" to receive a motivational quote.

## API Dependency

To generate side hustle ideas and money quotes, you **must** set up another project, **4_Simple APIs**. Follow these steps:

1. Clone the **4_Simple APIs** repository and navigate to its directory.
2. Install FastAPI using `Uv`:

   ```sh
   uv add fastapi[standard]
   ```

3. Run the FastAPI server:

   ```sh
   fastapi dev main.py
   ```

Once the FastAPI server is running, the Streamlit app will be able to fetch side hustle ideas and money quotes.

## Contact

For any questions, email **[ar3584158@gmail.com](mailto:ar3584158@gmail.com)**. Happy coding! 🚀

