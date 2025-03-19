# Personal Library Manager

## Overview
Personal Library Manager is a simple command-line application that allows users to manage their personal book collection. Users can add, remove, search, and display books, as well as view reading statistics. The program stores book data in a JSON file to retain information across sessions.

## Features
- Add books with details such as title, author, publication year, genre, and reading status.
- Remove books from the library.
- Search for books by title or author.
- Display all books in the collection.
- Show statistics on read and unread books.
- Save and load data using a JSON file.

## Requirements
- Python 3.x

## Installation
1. Clone this repository or download the script.
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Ensure you have Python installed on your system. You can check by running:
   ```sh
   python --version
   ```
3. No additional dependencies are required as this script uses built-in Python modules.

## Usage
Run the script in a terminal or command prompt:
```sh
python library_manager.py
```
Follow the on-screen menu options to interact with the library manager.

## File Structure
- `library_manager.py` - Main script containing the library management functionality.
- `library.json` - JSON file used for storing book data (automatically created and updated by the script).

## Data Storage
The script saves all book information in a `library.json` file in the following format:
```json
[
    {
        "title": "book title",
        "author": "author name",
        "publication_year": 2023,
        "genre": "fiction",
        "is_read": true
    }
]
```

## Contributing
If you have suggestions or want to improve this script, feel free to fork the repository and submit a pull request.

## License
This project is open-source and available under the MIT License.

