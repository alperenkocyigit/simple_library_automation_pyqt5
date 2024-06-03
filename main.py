import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
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

        # Connect buttons to functions
        self.pushButtonAddBook.clicked.connect(self.add_book)
        self.pushButtonUpdateBook.clicked.connect(self.update_book)
        self.pushButtonDeleteBook.clicked.connect(self.delete_book)
        
        self.pushButtonAddCategory.clicked.connect(self.add_category)
        self.pushButtonUpdateCategory.clicked.connect(self.update_category)
        self.pushButtonDeleteCategory.clicked.connect(self.delete_category)
        
        self.pushButtonAddAuthor.clicked.connect(self.add_author)
        self.pushButtonUpdateAuthor.clicked.connect(self.update_author)
        self.pushButtonDeleteAuthor.clicked.connect(self.delete_author)

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

    def add_book(self):
        title = self.lineEditBookTitle.text()
        category_id = self.lineEditBookCategory.text()
        author_id = self.lineEditBookAuthor.text()
        self.c.execute("INSERT INTO books (title, category_id, author_id) VALUES (?, ?, ?)", (title, category_id, author_id))
        self.conn.commit()
        self.load_books()

    def update_book(self):
        book_id = self.lineEditBookID.text()
        title = self.lineEditBookTitle.text()
        category_id = self.lineEditBookCategory.text()
        author_id = self.lineEditBookAuthor.text()
        self.c.execute("UPDATE books SET title = ?, category_id = ?, author_id = ? WHERE id = ?", (title, category_id, author_id, book_id))
        self.conn.commit()
        self.load_books()

    def delete_book(self):
        book_id = self.lineEditBookID.text()
        self.c.execute("DELETE FROM books WHERE id = ?", (book_id,))
        self.conn.commit()
        self.load_books()

    def add_category(self):
        name = self.lineEditCategoryName.text()
        self.c.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        self.conn.commit()
        self.load_categories()

    def update_category(self):
        category_id = self.lineEditCategoryID.text()
        name = self.lineEditCategoryName.text()
        self.c.execute("UPDATE categories SET name = ? WHERE id = ?", (name, category_id))
        self.conn.commit()
        self.load_categories()

    def delete_category(self):
        category_id = self.lineEditCategoryID.text()
        self.c.execute("DELETE FROM categories WHERE id = ?", (category_id,))
        self.conn.commit()
        self.load_categories()

    def add_author(self):
        name = self.lineEditAuthorName.text()
        self.c.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        self.conn.commit()
        self.load_authors()

    def update_author(self):
        author_id = self.lineEditAuthorID.text()
        name = self.lineEditAuthorName.text()
        self.c.execute("UPDATE authors SET name = ? WHERE id = ?", (name, author_id))
        self.conn.commit()
        self.load_authors()

    def delete_author(self):
        author_id = self.lineEditAuthorID.text()
        self.c.execute("DELETE FROM authors WHERE id = ?", (author_id,))
        self.conn.commit()
        self.load_authors()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryAutomation()
    window.show()
    sys.exit(app.exec_())
