import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi
import sqlite3

class LibraryAutomation(QMainWindow):
    def __init__(self):
        super(LibraryAutomation, self).__init__()
        loadUi("MainWindow.ui", self)
        self.conn = sqlite3.connect('books.db')
        self.c = self.conn.cursor()
        
        # Initialize tables
        self.setup_books_table()
        self.setup_categories_table()
        self.setup_authors_table()

        # Load initial data
        self.load_books()
        self.load_categories()
        self.load_authors()
        self.load_category_dropdown()
        self.load_author_dropdown()

        # Connect buttons to functions
        self.pushButtonAddBook.clicked.connect(self.add_book)
        self.pushButtonUpdateBook.clicked.connect(self.update_book)
        self.pushButtonDeleteBook.clicked.connect(self.confirm_delete_book)
        
        self.pushButtonAddCategory.clicked.connect(self.add_category)
        self.pushButtonUpdateCategory.clicked.connect(self.update_category)
        self.pushButtonDeleteCategory.clicked.connect(self.delete_category)
        
        self.pushButtonAddAuthor.clicked.connect(self.add_author)
        self.pushButtonUpdateAuthor.clicked.connect(self.update_author)
        self.pushButtonDeleteAuthor.clicked.connect(self.delete_author)

        self.pushButtonSearchBook.clicked.connect(self.search_books)

        # Connect table widget to select row
        self.tableWidgetBooks.itemSelectionChanged.connect(self.on_book_selection_changed)

    def setup_books_table(self):
        self.tableWidgetBooks.setColumnCount(4)
        self.tableWidgetBooks.setHorizontalHeaderLabels(["ID", "Title", "Category ID", "Author ID"])
        self.tableWidgetBooks.setColumnWidth(0, 50)
        self.tableWidgetBooks.setColumnWidth(1, 200)
        self.tableWidgetBooks.setColumnWidth(2, 100)
        self.tableWidgetBooks.setColumnWidth(3, 100)

    def setup_categories_table(self):
        self.tableWidgetCategories.setColumnCount(2)
        self.tableWidgetCategories.setHorizontalHeaderLabels(["ID", "Name"])
        self.tableWidgetCategories.setColumnWidth(0, 50)
        self.tableWidgetCategories.setColumnWidth(1, 250)

    def setup_authors_table(self):
        self.tableWidgetAuthors.setColumnCount(2)
        self.tableWidgetAuthors.setHorizontalHeaderLabels(["ID", "Name"])
        self.tableWidgetAuthors.setColumnWidth(0, 50)
        self.tableWidgetAuthors.setColumnWidth(1, 250)

    def load_books(self):
        self.c.execute("SELECT * FROM books")
        books = self.c.fetchall()
        self.tableWidgetBooks.setRowCount(len(books))
        for row_num, row_data in enumerate(books):
            for col_num, col_data in enumerate(row_data):
                self.tableWidgetBooks.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

    def load_categories(self):
        self.c.execute("SELECT * FROM categories")
        categories = self.c.fetchall()
        self.tableWidgetCategories.setRowCount(len(categories))
        for row_num, row_data in enumerate(categories):
            for col_num, col_data in enumerate(row_data):
                self.tableWidgetCategories.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

    def load_authors(self):
        self.c.execute("SELECT * FROM authors")
        authors = self.c.fetchall()
        self.tableWidgetAuthors.setRowCount(len(authors))
        for row_num, row_data in enumerate(authors):
            for col_num, col_data in enumerate(row_data):
                self.tableWidgetAuthors.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

    def load_category_dropdown(self):
        self.comboBoxBookCategory.clear()
        self.c.execute("SELECT id, name FROM categories")
        categories = self.c.fetchall()
        for category in categories:
            self.comboBoxBookCategory.addItem(category[1], category[0])

    def load_author_dropdown(self):
        self.comboBoxBookAuthor.clear()
        self.c.execute("SELECT id, name FROM authors")
        authors = self.c.fetchall()
        for author in authors:
            self.comboBoxBookAuthor.addItem(author[1], author[0])

    def add_book(self):
        title = self.lineEditBookTitle.text()
        category_id = self.comboBoxBookCategory.currentData()
        author_id = self.comboBoxBookAuthor.currentData()
        self.c.execute("INSERT INTO books (title, category_id, author_id) VALUES (?, ?, ?)", (title, category_id, author_id))
        self.conn.commit()
        self.load_books()

    def update_book(self):
        book_id = self.lineEditBookID.text()
        title = self.lineEditBookTitle.text()
        category_id = self.comboBoxBookCategory.currentData()
        author_id = self.comboBoxBookAuthor.currentData()
        self.c.execute("UPDATE books SET title = ?, category_id = ?, author_id = ? WHERE id = ?", (title, category_id, author_id, book_id))
        self.conn.commit()
        self.load_books()

    def confirm_delete_book(self):
        selected_row = self.tableWidgetBooks.currentRow()
        if selected_row != -1:
            book_id = self.tableWidgetBooks.item(selected_row, 0).text()
            book_title = self.tableWidgetBooks.item(selected_row, 1).text()
            reply = QMessageBox.question(self, 'Confirm Delete', f"Are you sure you want to delete the book '{book_title}'?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.delete_book(book_id)
        else:
            QMessageBox.warning(self, 'No Selection', 'Please select a book to delete.')

    def delete_book(self, book_id):
        self.c.execute("DELETE FROM books WHERE id = ?", (book_id,))
        self.conn.commit()
        self.load_books()

    def add_category(self):
        name = self.lineEditCategoryName.text()
        self.c.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        self.conn.commit()
        self.load_categories()
        self.load_category_dropdown()

    def update_category(self):
        category_id = self.lineEditCategoryID.text()
        name = self.lineEditCategoryName.text()
        self.c.execute("UPDATE categories SET name = ? WHERE id = ?", (name, category_id))
        self.conn.commit()
        self.load_categories()
        self.load_category_dropdown()

    def delete_category(self):
        category_id = self.lineEditCategoryID.text()
        self.c.execute("DELETE FROM categories WHERE id = ?", (category_id,))
        self.conn.commit()
        self.load_categories()
        self.load_category_dropdown()

    def add_author(self):
        name = self.lineEditAuthorName.text()
        self.c.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        self.conn.commit()
        self.load_authors()
        self.load_author_dropdown()

    def update_author(self):
        author_id = self.lineEditAuthorID.text()
        name = self.lineEditAuthorName.text()
        self.c.execute("UPDATE authors SET name = ? WHERE id = ?", (name, author_id))
        self.conn.commit()
        self.load_authors()
        self.load_author_dropdown()

    def delete_author(self):
        author_id = self.lineEditAuthorID.text()
        self.c.execute("DELETE FROM authors WHERE id = ?", (author_id,))
        self.conn.commit()
        self.load_authors()
        self.load_author_dropdown()

    def search_books(self):
        search_text = self.lineEditSearchBook.text()
        query = f"SELECT * FROM books WHERE title LIKE ?"
        self.c.execute(query, (f'%{search_text}%',))
        books = self.c.fetchall()
        self.tableWidgetBooks.setRowCount(len(books))
        for row_num, row_data in enumerate(books):
            for col_num, col_data in enumerate(row_data):
                self.tableWidgetBooks.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

    def on_book_selection_changed(self):
        selected_row = self.tableWidgetBooks.currentRow()
        if selected_row != -1:
            self.lineEditBookID.setText(self.tableWidgetBooks.item(selected_row, 0).text())
            self.lineEditBookTitle.setText(self.tableWidgetBooks.item(selected_row, 1).text())
            category_id = self.tableWidgetBooks.item(selected_row, 2).text()
            author_id = self.tableWidgetBooks.item(selected_row, 3).text()
            self.comboBoxBookCategory.setCurrentIndex(self.comboBoxBookCategory.findData(int(category_id)))
            self.comboBoxBookAuthor.setCurrentIndex(self.comboBoxBookAuthor.findData(int(author_id)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryAutomation()
    window.show()
    sys.exit(app.exec_())
