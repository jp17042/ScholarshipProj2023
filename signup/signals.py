from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import connection
import sqlite3

def create_user_table(user_id):
    # Generate a unique table name based on the user's ID
    table_name = 'user_{0}_data'.format(user_id)

    # Connect to the SQLite database
    conn = sqlite3.connect('/Users/jacobptak/Documents/GitHub/ScholarshipProj2023/database.sqlite3')
    cursor = conn.cursor()

    # Execute the raw SQL query to create the table
    create_table_query = 'CREATE TABLE {0} (Question_Number TEXT, Survey_Name TEXT, Question_Type TEXT, Question_Text TEXT)'.format(table_name)
    cursor.execute(create_table_query)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()