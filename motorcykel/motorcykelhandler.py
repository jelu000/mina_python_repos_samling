#https://antares-sql.app/downloads
#https://pynative.com/python-sqlite/#h-create-sqlite-table-from-python
#https://www.sqlite.org/autoinc.html

import sqlite3
from sqlite3 import Error

import motorcykel


class MotorcykelHandler:

    def __init__(self):
        

        self.db_name = "motorcyklar.db"
        t_bike = motorcykel.Motorcykel()
        #t_bike = motorcykel.Motorcykel(1,"Honda", "CB", 125, 180, 12, 110)
        t_bike.setFabrikat("Honda")
        
        print(f"Motorcykel Handler: {t_bike.getFabrikat()}")
        
        self.create_conn_sqllite(self.db_name)
        self.create_table()
        


    def addMotorcykel(self, t_motorcykel: motorcykel.Motorcykel):
      
        sqliteConnection = sqlite3.connect(self.db_name)
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = f"""INSERT INTO motorcyklar
                          (fabrikat, modell, kubik, vikt, hk, topphastighet)  
                          VALUES  
                          ('{t_motorcykel.fabrikat}', '{t_motorcykel.modell}', {t_motorcykel.kubik}, {t_motorcykel.vikt}, {t_motorcykel.hk}, {t_motorcykel.topphastighet}) """
        

        #print(sqlite_insert_query)
        #input("Vänta")
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

        

    def create_conn_sqllite(self, db_file):
        # create a database connection to a SQLite database
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

        return conn
    
    #Skapar tabellen i databasen, körs bara första gången
    def create_table(self):
        try:
            sqliteConnection = sqlite3.connect(self.db_name)
            sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS motorcyklar (
                                id INTEGER PRIMARY KEY,
                                fabrikat TEXT NOT NULL,
                                modell TEXT,
                                kubik INTEGER,
                                vikt INTEGER,
                                hk INTEGER,
                                topphastighet INTEGER);'''

            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            print("SQLite table created")

            cursor.close()

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")

