import mysql.connector

class Database:
    def dbconnection(self):
        return mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Nikhil@2003",
            database="pharma_choice_db"
        )