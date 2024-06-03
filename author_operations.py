//This class controls author updates in mysql database 

class Author_Operations:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def update_author(self, author_id, new_name, new_biography):
        query = "UPDATE authors SET name = %s, biography = %s WHERE id = %s"
        data = (new_name, new_biography, author_id)
        self.db_manager.execute_query(query, data)
