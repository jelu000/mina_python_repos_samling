import sqlite3
from sqlite3 import Error

#create table dogs (id integer primary key, namn text, ras text);
#insert into dogs (namn, ras) values("torin", "perro");
#https://www.sqlitetutorial.net/download-install-sqlite/
#https://www.sqlite.org/quickstart.html
#https://www.tutorialspoint.com/sqlite/


class Dog:

    def __init__(self, id=None, namn=None, ras=None):
        self.id = id
        self.namn = namn
        self.ras = ras
        
        self.db_name = "dogs.db"

    #Create
    def add_dog(self, namn, ras):

        dog_list = []

        sqliteConnection = sqlite3.connect(self.db_name)
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = f"""INSERT INTO dogs
                          (namn, ras)  
                          VALUES  
                          ('{namn}', '{ras}') """
        

        #print(sqlite_insert_query)
        #input("Vänta")
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()
        dog_list = self.get_dog_list()
        return dog_list 
    
    #Read
    def get_dog_list(self):

        dog_list = []

        try:
            sqliteConnection = sqlite3.connect(self.db_name)
            cursor = sqliteConnection.cursor()
            #print("Connected to SQLite")

            sqlite_select_query = """SELECT * from dogs ORDER BY namn"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
              
            for row in records:
                
                
                hund_id=row[0]
                hund_namn=row[1]
                hund_ras=row[2]
                dog_list.append(Dog(hund_id, hund_namn, hund_ras))
                
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

        return dog_list


    #Update
    def update_dog(self, id, name, ras):

        return self.dog_list
    
    #Delete
    def delete_dog(self, id):
        return self.dog_list


