#!/usr/bin/env python3
import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (update host, user, password if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"   # <-- Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
