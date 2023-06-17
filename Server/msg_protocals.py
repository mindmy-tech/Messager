# import mysql.connector as sql

from cs50 import SQL as sql


class Protocols:

    def __init__(self):
        self.db = sql("sqlite:///messages.db")

    # @staticmethod
    # def post_protocol(data):
    #     conn = sql.connect(host="localhost", user='root', password='root', database='test')
    #     if conn:
    #         cursor = conn.cursor()
    #         query = f'INSERT INTO CHAT_MESSAGES(USER_ID, USERNAME, CHATROOM_ID, MESSAGE) ' \
    #                 f'VALUES("{data["USER_ID"]}","{data["USERNAME"]}", "{data["CHATROOM"]}", "{data["MESSAGE"]}")'
    #         cursor.execute(query)
    #         conn.commit()
    #         conn.close()
    #         print('record added !')
    #     else:c
    #         print("error")

    # @staticmethod
    # def get_protocol(data):
    #     conn = sql.connect(host="localhost", user='root', password='root', database='test')
    #     if conn:
    #         cursor = conn.cursor()
    #         query = f'select * from chat_messages where message_id> {data["last_msg"]}'
    #         cursor.execute(query)
    #         data = [i for i in cursor.fetchall()]
    #         conn.close()
    #         return data
    #     else:
    #         print("error")

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



pro = Protocols()

pro.init_db()