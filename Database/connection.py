import pyodbc
from config import DB_CONNECTION

def get_connection():
    return pyodbc.connect(DB_CONNECTION)