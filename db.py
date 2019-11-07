import mysql.connector

cnx = mysql.connector.connect(user='pawelwr5', password='xxx',
                            host='pawelwr5.mysql.eu.pythonanywhere-services.com',
                            database='pawelwr5$blackjack')



cursor = cnx.cursor()

cnx.close()
