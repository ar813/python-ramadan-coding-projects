# Todo List CLI Application

## Overview

This is a simple command-line interface (CLI) Todo List application built using Python and Click (it is a Python package that helps developers to create command-line interface applications). It allows users to manage their tasks efficiently by adding, listing, completing, and removing tasks. The tasks are stored in a JSON file (`todo.json`) to persist data.

## Features

- ✏️ Add new tasks
- 📋 Show your task list
- ✅ Mark tasks as done
- 🗑️ Delete tasks you don't need

## Quick Start Guide

### 1. Setup (One-time only)

1. Install uv (copy and paste this in PowerShell):

   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. Set up the project:

   **Initialize the project with uv**

   ```sh
   uv init .
   ```

   **Add Click package**

   ```sh
   uv add click
   ```

   **Activate the virtual environment**

   ```sh
   .venv\Scripts\activate
   ```

### 2. Using the App

Here are the basic commands you'll need:

1. **Start the application**

   ```sh
   python todo.py
   ```

   ```sh
   uv run python todo.py
   ```

2. **Add a task**

   ```sh
   python todo.py add "Buy groceries"
   ```

   ```sh
   uv run python todo.py add "Buy groceries"
   ```

3. **See your tasks**

   ```sh
   python todo.py list
   ```

   ```sh
   uv run python todo.py list
   ```

   You'll see something like:

   ```
   1. Buy groceries [❌]
   2. Call mom [✔️]
   ```

   (✔️ = done, ❌ = not done)

4. **Mark a task as done**

   ```sh
   python todo.py complete 1
   ```

   ```sh
   uv run python todo.py complete 1
   ```

   (Replace 1 with your task's number)

5. **Delete a task**

   ```sh
   python todo.py remove 1
   ```

   ```sh
   uv run python todo.py remove 1
   ```

   (Replace 1 with your task's number)

## Difference Between `uv run python todo.py` and `python todo.py`

Both commands are used to run the application, but there are key differences:

### `python todo.py`

- Runs the `todo.py` script using the system's Python installation.
- If you have multiple versions of Python installed, it might use the wrong one.
- It may not work if the required libraries (like Click) are not installed in the global Python environment.

### `uv run python todo.py`

- Runs the script inside a virtual environment managed by `uv`.
- Ensures that the correct dependencies (like Click) are available.
- Helps avoid conflicts between different projects with different dependencies.

### When to Use Which?

- Use `python todo.py` if everything is installed globally and working fine.
- Use `uv run python todo.py` if you're working inside a virtual environment and want to avoid dependency issues.

## Need Help?

- Make sure Python is installed on your computer
- All your tasks are saved automatically in a file called `todo.json`
- Task numbers show the order in which you added them

## Technical Details (For Developers)

- Built with Python and Click
- Uses JSON for data storage
- Files in the project:
  - `todo.py`: The main program
  - `todo.json`: Where your tasks are saved
  - `.venv`: Contains Python and required packages

