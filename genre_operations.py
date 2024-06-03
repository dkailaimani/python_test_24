//Updates genre operations in mysql database

class Genre_Operations:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def update_genre(self, genre_id, new_name, new_description, new_category):
        query = "UPDATE genres SET name = %s, description = %s, category = %s WHERE id = %s"
        data = (new_name, new_description, new_category, genre_id)
        self.db_manager.execute_query(query, data)
