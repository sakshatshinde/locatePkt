import sqlite3
from sqlite3 import  Error

#global
conn = None

try:
    conn = sqlite3.connect(':memory:')
    print(sqlite3.version)

    dbCursor = conn.cursor()

    # Table creation
    dbCursor.execute('''
    
    CREATE TABLE location (
        IP          text        NOT NULL,
        country     text        NOT NULL,
        longitude   decimal     NOT NULL,
        latitude    decimal     NOT NULL
        )
    
    ''')

except Error as e:
    print(e)
    
def closeConn():
    if conn:
        conn.close()

# def insertInto(countryName :str, long, lat):
#     dbString = f"INSERT INTO location (country,longitude,latitude) VALUES ('{countryName}', {long}, {lat})"
#     print(dbString)
#     dbCursor.execute(dbString)
#     conn.commit()

def insertInto(locationList):
    dbCursor.executemany(
        'INSERT INTO location (IP,country,longitude,latitude) VALUES (?,?,?,?)', locationList
    )

if __name__ == '__main__':

    locationList = [('120.0.0.1', 'India', 19.075983, 72.877655),
                    ('162.159.133.234','Indioa', 19.075783, 72.877655),
                    ]
    insertInto(locationList)
    # insertInto('Indioa', 19.075783, 72.877655)
    dbCursor.execute("SELECT * FROM location")
    print(dbCursor.fetchall())
    closeConn()