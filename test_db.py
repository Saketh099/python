import mysql.connector

config = {
    "user": "mysqluser",
    "password": "*7E567C9DC06217268D72D52BABCA14EAB8993ACF",
    "host": "104.237.2.219",
    "port": "5340",
    "database": "customer_support"
}

try:

    connection = mysql.connector.connect(**config)
    
    if connection.is_connected():
        print("✅ Connected to MySQL server successfully!")
        cursor = connection.cursor()
        query = "SELECT * FROM tickets LIMIT 5;"
        cursor.execute(query)
        rows = cursor.fetchall()
        if rows:
            print("\n🎯 Sample Data from 'tickets' table:")
            for row in rows:
                print(row)
        else:
            print("⚠️ No data found in the 'tickets' table.")
        
        cursor.close()

    else:
        print("❌ Failed to connect to MySQL.")

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("✅ Connection closed.")
