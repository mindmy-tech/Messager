# import mysql.connector as sql

from cs50 import SQL as sql


class Protocols:

    def __init__(self):
        try :
            self.db = sql("sqlite:///messages.db")
        except:
            open("messages.db", 'w')
            self.db = sql("sqlite:///messages.db")

        self.init_db()

    def post_protocol(self, data):
        if data:
            query = " INSERT INTO messages(user_id, message ) values(?, ?)"
            self.db.execute(query, data["USERNAME"], data["MESSAGE"] )

    def get_protocol(self, data):
        if data:
            query = "SELECT user_id, message , msg_at FROM messages WHERE id > ? ORDER BY msg_at"
            value = self.db.execute(query, data["last_msg"])
            print(value)
            return value


    def init_db(self):

        #  Users table
        #  to handle users data 
        query1 = """
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        """
        query2 ="CREATE INDEX IF NOT EXISTS idx_users_name ON users (name);"


        #  store messages 

        query3 ="""CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        message TEXT NOT NULL,
        msg_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        querys = [query1, query2, query3]

        for query in querys:
            self.db.execute(query)


