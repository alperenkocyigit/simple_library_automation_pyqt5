# Library Automation System

This is a Library Automation System built using PyQt5 and SQLite. The application allows users to manage books, categories, and authors with basic CRUD operations.

## Features

- **Books Management**: Add, update, delete, and search for books.
- **Categories Management**: Add, update, and delete book categories.
- **Authors Management**: Add, update, and delete authors.
- **Dropdown Menus**: Select categories and authors from dropdown menus when adding or updating books.
- **Confirmation Dialog**: Confirm before deleting a book.
- **Search Functionality**: Search for books by title.

## Prerequisites

- Python 3.x
- PyQt5
- SQLite3

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/alperenkocyigit/simple_library_automation_pyqt5
   cd simple_library_automation_pyqt5
   ```

2. **Install the required packages:**
   ```bash
   pip install pyqt5
   ```

3. **Set up the SQLite database:**
   ```bash
   python setup_database.py
   ```

## Usage

1. **Run the application:**
   ```bash
   python main.py
   ```

1. **Main Window:**
    * The main window consists of a tab widget with four tabs: Main Menu, Books, Categories, and Authors.

2. **Books Tab:**
    * Use the fields to add or update book details.
    Use the dropdown menus to select a category and an author.
    * Click "Add" to add a new book, "Update" to update the selected book, or "Delete" to delete the selected book.
    Use the search bar to filter books by title.
    Categories Tab:

    * Use the fields to add or update category details.
    Click "Add" to add a new category, "Update" to update the selected category, or "Delete" to delete the selected category.
3. **Authors Tab:**

    * Use the fields to add or update author details.
    * Click "Add" to add a new author, "Update" to update the selected author, or "Delete" to delete the selected author.

4. **Code Structure:**
    **main.py**: The main application file that contains the logic for the GUI and CRUD operations.
    **MainWindow.ui**: The UI file designed using Qt Designer.
    **setup_database.py**: Script to set up the SQLite database and create the required tables.

## Author
    This project was coded by Alperen KOÇYİĞİT.