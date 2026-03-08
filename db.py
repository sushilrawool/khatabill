import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="khatabill_user",
        password="khatabill_pass",
        database="khatabill"
    )