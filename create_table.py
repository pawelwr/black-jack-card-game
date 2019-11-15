import mysql.connector

config = {'user': 'pawelwr5', 'password': '20python19',
        'host': 'pawelwr5.mysql.eu.pythonanywhere-services.com',
        'database': 'pawelwr5$blackjack'}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = """CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,
        username char(20), account_status int, played_games int,
        won_games int);
        """

cursor.execute(query)

query = """CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY,
        winner_id int, bet int,
        FOREIGN KEY (winner_id) REFERENCES users (id)
        );
        """

cursor.execute(query)

cnx.close()
