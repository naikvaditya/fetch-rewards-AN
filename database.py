import psycopg2
connection = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port=5432)
cursor = connection.cursor()
cursor.execute("select * from user_logins;")
records = cursor.fetchall()
print(records)


