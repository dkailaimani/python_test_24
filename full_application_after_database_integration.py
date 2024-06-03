//Library management system operations integrated w MySql database

import sys
sys.path.append('C:\\users\\student\\appdata\\local\\programs\\python\\python312\\lib\\site-packages')

import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="XyZ$9#1@7QwEeTy",
            database="Library_Management_System"
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query, data=None):
        try:
            if data:
                self.cursor.execute(query, data)
            else:
                self.cursor.execute(query)
            self.conn.commit()
        except mysql.connector.Error as err:
            print("MySQL Error:", err)

    def fetch_query(self, query, data=None):
        try:
            if data:
                self.cursor.execute(query, data)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print("MySQL Error:", err)
            return None

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

class Author_Operations:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def update_author(self, author_id, new_name, new_biography):
        query = "UPDATE authors SET name = %s, biography = %s WHERE id = %s"
        data = (new_name, new_biography, author_id)
        self.db_manager.execute_query(query, data)

class Genre_Operations:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def update_genre(self, genre_id, new_name, new_description, new_category):
        query = "UPDATE genres SET name = %s, description = %s, category = %s WHERE id = %s"
        data = (new_name, new_description, new_category, genre_id)
        self.db_manager.execute_query(query, data)

class BorrowedBook_Operations:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def update_borrowed_book(self, book_id, user_id, borrow_date, return_date):
        query = "UPDATE borrowed_books SET user_id = %s, borrow_date = %s, return_date = %s WHERE id = %s"
        data = (user_id, borrow_date, return_date, book_id)
        self.db_manager.execute_query(query, data)

class User_Operations:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def update_user(self, user_id, new_name, new_library_id):
        query = "UPDATE users SET name = %s, library_id = %s WHERE id = %s"
        data = (new_name, new_library_id, user_id)
        self.db_manager.execute_query(query, data)

if __name__ == "__main__":
    db_manager = DatabaseManager()
    author_operations = Author_Operations(db_manager)
    genre_operations = Genre_Operations(db_manager)
    borrowed_book_operations = BorrowedBook_Operations(db_manager)
    user_operations = User_Operations(db_manager)

    db_manager.close_connection()
