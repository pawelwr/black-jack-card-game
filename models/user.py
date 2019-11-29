import sqlite3


class Player:
    def __init__(self, id, name, account=5000, played_games=0, won_games=0):
        self.id = 0
        self.name = name
        self.account = 5000
        self.played_games = 0
        self.won_games = 0

    @classmethod
    def is_user(cls, username):

        conn = sqlite3.connect('bj.db')
        c = conn.cursor()
        query = "SELECT FROM users WHERE username={}".format(username)
        c.execute(query)

        if c.fetchone():
            return True
        return False

    def new_user(self, username):
        if self.is_user(username):
            return {"message": "User allready exist"}
        conn = sqlite3.connect('bj.db')
        c = conn.cursor()
        query = "INSERT INTO users VALUES ({}, {}. {}. {})".format(
            self.name, self.account, self.played_games, self.won_games)
        c.execute(query)
        return {"message": "User has been created succesfully"}

    @classmethod
    def load_user(cls, username):
        conn = sqlite3.connect('bj.db')
        c = conn.cursor()
        query = "SELECT FROM users WHERE username='{}'".format(username)
        c.execute(query)
        return c.fetchone()

    # def save_user(self):
    #     conn = sqlite3.connect('bj.db')
    #     c = conn.cursor()
    #     query = """UPDATE users
    #     account = '{}'
    #     played_games = '{}'
    #     won_games = '{}'
    #     WHERE username = '{}'
    #     """.format(#############)