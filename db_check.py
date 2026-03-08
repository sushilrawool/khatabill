import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="khatabill_user",       # new user
        password="khatabill_pass",   # password
        database="khatabill"         # database name
    )
    
    if conn.is_connected():
        print("✅ Database connected successfully!")
    else:
        print("❌ Connection failed.")

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
