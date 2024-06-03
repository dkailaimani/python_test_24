//Updates user table in mysql database

class User_Operations:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def update_user(self, user_id, new_name, new_library_id):
        query = "UPDATE users SET name = %s, library_id = %s WHERE id = %s"
        data = (new_name, new_library_id, user_id)
        self.db_manager.execute_query(query, data)
