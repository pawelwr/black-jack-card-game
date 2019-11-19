import sqlite3
conn = sqlite3.connect('bj.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS test
            (rowid NOT NULL,
            username varchar unique, 
            account_status int,
            played_games int, 
            won_games int)""")

c.execute("""CREATE TABLE IF NOT EXISTS played_games
            (winner int,
            bet int,
            computer_points int,
            user_points int,
            FOREIGN KEY (winner)
            REFERENCES test (rowid))""")

conn.commit()
conn.close()