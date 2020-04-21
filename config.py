import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
username, password, port, dbname = 'postgres', '7490', 5432, 'fyyur'
SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{password}@localhost:{port}/{dbname}"
