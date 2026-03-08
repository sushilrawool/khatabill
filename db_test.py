import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2003",  # तुमचा MySQL password
    database="khatabill"
)

cursor = db.cursor()
cursor.execute("SELECT DATABASE();")
print("Connected to database:", cursor.fetchone())

cursor.close()
db.close()
