import os
import sqlite3
from sqlite3 import Error

#main()--------------------------------------
def main():

    while True:
        add_dog_to_table()
        list_dog_table()

        svar = input("\nVill du mata in en hund till j/n: ")
        if (svar != "j"):
            break

#add_dog_to_table() - Create new dog in DB------------
def add_dog_to_table():
    os.system('cls' if os.name == 'nt' else 'clear')
    hundnamn = input("Mata in hundnamn: ")
    hundras = input("Mata in hundras: ")

    sqliteConnection = sqlite3.connect("dogs.db")
    cursor = sqliteConnection.cursor()
    sqlite_insert_query = f"""INSERT INTO dogs
                          (namn, ras)  
                          VALUES  
                          ('{hundnamn}', '{hundras}') """
        
    
    cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("\nLa till Hund till DB\n")
    #stänger cursor objektet    
    cursor.close()
    #stänger conection
    sqliteConnection.close()


#list_dog_table()-READ from DB----------- 
def list_dog_table():

    #Skapar DB connection och databas fråga som sen körs/executes
    sqliteConnection = sqlite3.connect("dogs.db")
    cursor = sqliteConnection.cursor()
    #print("Connected to SQLite")
    sqlite_select_query = """SELECT * from dogs ORDER by namn"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    #Lägger till varje hund i databasen till hundlistan  
    for row in records:
        print(f"\tID: {row[0]},\tNAMN: {row[1]}, \tRAS: {row[2]}")
        
    #stänger cursor objektet    
    cursor.close()
    #stänger conection
    sqliteConnection.close()
    print("The SQLite connection is closed")

main()
