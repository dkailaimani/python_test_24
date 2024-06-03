class BorrowedBook_Operations:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def update_borrowed_book(self, book_id, user_id, borrow_date, return_date):
        query = "UPDATE borrowed_books SET user_id = %s, borrow_date = %s, return_date = %s WHERE id = %s"
        data = (user_id, borrow_date, return_date, book_id)
        self.db_manager.execute_query(query, data)
