import sqlite3
from sqlite3 import  Error

def createConn():
    conn = None
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
    
    except Error as e:
        print(e)
    
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    createConn()