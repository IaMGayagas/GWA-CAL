import sqlite3
import models

class DbHandler:
    def __init__(self):
        self.dbname = 'database.db'
        self.users_table='users_table'

        self.conn= sqlite3.connect(self.dbname)
        self.cursor= self.conn.cursor()

        table_queries = [f"CREATE TABLE IF NOT EXISTS {self.users_table} (id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, username TEXT, password TEXT, email TEXT)"]
        
        for query in table_queries:
            self.cursor.execute(query)
            self.conn.commit()

    def create_user(self, user: models.User):
        insert_query = f"INSERT INTO {self.users_table} (email, firstname, lastname, username, password) VALUES (?,?, ?, ?, ?)"
        insert_values = (user.email, user.firstname, user.lastname, user.username, user.password)
        self.cursor.execute(insert_query, insert_values)
        self.conn.commit()

    def login_credential(self, username, password):
        query = f"SELECT username, password FROM {self.users_table} WHERE username = ? AND password = ?"
        values = (username, password)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        return result
    
    def check_email_exists(self, email):
        query = f"SELECT COUNT(*) FROM {self.users_table} WHERE email = ?"
        self.cursor.execute(query, (email,))
        result = self.cursor.fetchone()
        return result[0] > 0
    
    def check_username_exists(self, username):
        query = f"SELECT COUNT(*) FROM {self.users_table} WHERE username = ?"
        self.cursor.execute(query, (username,))
        result = self.cursor.fetchone()
        return result[0] > 0

    def update_password(self, email, new_password):
        update_query = f"UPDATE {self.users_table} SET password = ? WHERE email = ?"
        update_values = (new_password, email)
        self.cursor.execute(update_query, update_values)
        self.conn.commit()


handler = DbHandler() 

        
