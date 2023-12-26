# database.py

import mysql.connector
from dotenv import load_dotenv
import os
from db_config import db_config, table

load_dotenv()

def connect_to_database():
    return mysql.connector.connect(**db_config)

def create_table_if_not_exists():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(table)
    connection.commit()
    connection.close()

def save_to_database(data):
    connection = connect_to_database()
    cursor = connection.cursor()

    create_table_if_not_exists()  # Ensure the table exists

    # Insert OCR result into the database
    insert_query = "INSERT INTO ocr_results (url, sql_i, xss, data) VALUES ('www.facebook.com', true, false, %s)"
    cursor.execute(insert_query, (data,))

    connection.commit()
    connection.close()
