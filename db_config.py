#chat template
import pyodbc

def get_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=YOUR_SERVER_NAME;'
        'DATABASE=YOUR_DATABASE_NAME;'
        'UID=YOUR_USERNAME;'
        'PWD=YOUR_PASSWORD'
    )
    return conn
