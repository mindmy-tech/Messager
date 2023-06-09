from cs50 import SQL


class Protocol:
    def __init__(self):
        """
        checks if the db file exists or else
        creates them"""
        try :
            self.db = SQL("sqlite:///messages.db")
        
        except:
            open("messages.db", 'w')
            self.db = SQL("sqlite:///messages.db")

        self.init_db()

    def post_protocol(self, data):
        """
        INSERTS MSG INTO THE DB ON TABLE MESSAGES
        """
        if data:
            query = " INSERT INTO messages(user_id, message ) values(?, ?)"
            self.db.execute(query, data["USERNAME"], data["MESSAGE"] )

    def get_protocol(self, data):
        """
        NOTE NOT IMPLEMENTED YET 
        """
        if data:
            query = "SELECT user_id, message , msg_at FROM messages WHERE id > ? ORDER BY msg_at"
            value = self.db.execute(query, data["last_msg"])
            print(value)
            return value


    def init_db(self):
        """
        Creates  table if it doent exists
        """

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

        # Executes all the query
        querys = [query1, query2, query3]

        for query in querys:
            self.db.execute(query)


