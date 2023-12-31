import sqlite3
from sqlite3 import Error
import dog
#create table dogs (id integer primary key, namn text, ras text);
#insert into dogs (namn, ras) values("torin", "perro");
#https://www.sqlitetutorial.net/download-install-sqlite/
#https://www.sqlite.org/quickstart.html
#https://www.tutorialspoint.com/sqlite/

class dogs_handler:

    def __init__(self):
        self.db_name = "dogs.db"

    #Create - add_dog()-------------------------------------------------------------------
    def add_dog(self, namn, ras):

        sqliteConnection = sqlite3.connect(self.db_name)
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = f"""INSERT INTO dogs
                          (namn, ras)  
                          VALUES  
                          ('{namn.capitalize()}', '{ras.capitalize()}') """
        
        #print(sqlite_insert_query)
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()
        
    #Read - get_dog_list()---------------------------------------------------------------------
    def get_dog_list(self):

        dog_list = []

        try:
            #Skapar DB connection och databas fråga som sen körs/executes
            sqliteConnection = sqlite3.connect(self.db_name)
            cursor = sqliteConnection.cursor()
            #print("Connected to SQLite")
            sqlite_select_query = """SELECT * from dogs ORDER BY namn"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            #Lägger till varje hund i databasen till hundlistan  
            for row in records:
                hund_id=row[0]
                hund_namn=row[1]
                hund_ras=row[2]
                dog_list.append(dog.dog(hund_id, hund_namn, hund_ras))
            #stänger cursor objektet    
            cursor.close()
        #skriver ut fel om det uppstår
        except sqlite3.Error as error:
            print("Get_dog_list()-Failed to read data from sqlite table", error)
        #stänger databas koppling 
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

        return dog_list
  
    #Update - Dog--------------------------------------
    def update_dog(self, id, name, ras):
        #print("inte klar, ska uppdatera hund i databas")
        int_id = int(id)

        # Use a parameterized query
        #sqlite_insert_query = f"""UPDATE dogs SET namn = ?, ras = ? WHERE id = {int_id}
        #VALUES = ('{name}', '{ras}', {int_id});"""

        sqlite_insert_query = f"""UPDATE dogs SET namn='{name}', ras='{ras}' WHERE id={id}; """
            
        print(sqlite_insert_query) 

        try:
            sqliteConnection = sqlite3.connect("dogs.db")
            cursor = sqliteConnection.cursor()
            #sqlite_insert_query = f"""UPDATE dogs
                            #SET namn={name},
                            #ras={ras}  
                            #WHERE id={id};  
                            #"""
            
            # Use a parameterized query
            #sqlite_insert_query = f"""UPDATE dogs SET namn = ?, ras = ? WHERE id = {int_id}
            #VALUES = ('{name}', '{ras}', {int_id});"""
            
        
            cursor.execute(sqlite_insert_query)
            sqliteConnection.commit()
            print(f"\nupdate_dog() {id}=id, {name}=namn , {ras}=ras  \n")
            #stänger cursor objektet    
            cursor.close()
            #stänger conection
            sqliteConnection.close()
        except sqlite3.Error as error:
            print("update_dog()-Failed to read data from sqlite table", error)
            
        #stänger databas koppling 
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
        
    
    #Delete - delete_dog-----------------------------
    def delete_dog(self, id):
        
        try:
            sqliteConnection = sqlite3.connect(self.db_name)
            cursor = sqliteConnection.cursor()
        
            sql_update_query = """DELETE from dogs where id = ?"""
            cursor.execute(sql_update_query, (id,))
            sqliteConnection.commit()
            cursor.close()
            print("hund bortagen")
        
        except sqlite3.Error as error:
            print("kunde inte tabort hund! ", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")
        
        