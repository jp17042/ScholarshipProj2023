from django.conf import settings
from django.db import connection
import os
def create_user_database(database_name):
    # Determine the path where the SQLite database file will be created
    db_file_path = os.path.join('/Users/jacobptak/Documents/GitHub/ScholarshipProj2023/django_project/db_folder', f'{database_name}.sqlite')

    # Create an empty file at the specified path
    with open(db_file_path, 'w'):
        pass