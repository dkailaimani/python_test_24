//This class connects to the mysql database and throws appropriate exceptions

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
