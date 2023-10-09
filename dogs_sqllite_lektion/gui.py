# coding=
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import dogs_handler

dogs_object = dogs_handler.dogs_handler()

root = Tk()  # create root window
root.title("Hundar")
root.geometry("600x400")

#Top panel ----------------------
pTop = PanedWindow()
pTop.pack(fill=BOTH, expand=1)

#emtyFields()--------------------------------------------
def emtyFields():
    tfNamn.delete("0", "end")
    tfRas.delete("0", "end")
    labelId.config(text="")

#updateListBox()----------------------------------------------
def updateListBox():
    #tabell.delete(0, END)
    #listbox_dogs.delete(0, END)
    tabell.delete(*tabell.get_children())  # Delete all items

    lista_dogs = dogs_object.get_dog_list()
    
    #for i, dog in enumerate(lista_dogs):
        #listbox_dogs.insert(dog.id,  f"Id: {dog.id},    Namn: {dog.namn},   Ras: {dog.ras} ")

    for i, dog in enumerate(lista_dogs):
        tabell.insert("", tk.END,  values=(dog.id, dog.namn, dog.ras))

#upateButtonEvent------------------------------------------------------------
def updateButtonEvent():

    hundnamn = tfNamn.get()
    hundras = tfRas.get()
    hund_id = labelId.cget("text")

    try:        
        if hund_id == "" and hundnamn != "":
            dogs_object.add_dog(hundnamn,hundras)
            #updateListBox()

        else:
            print("Uppdatera hund")
            #dogs_object.update_dog(int(aktivt_id), hundnamn, hundras)

        
        updateListBox()
        emtyFields()

    except ValueError:
       messagebox.showerror("ERroR!")

#delButtonEvent()-----------------------------------------
def delButtonEvent():
    t_id=labelId.cget("text")
    print(f"Tabort hund id = {t_id}")
    try:
        # provar att tabort hund
        if (t_id != ""):
            dogs_object.delete_dog(int(t_id))
            
        else:
            messagebox(f"Kunde inte tabort hund med id: {t_id}")

    except SystemError as e:
        messagebox(f"Något gick fel")

    updateListBox()
    emtyFields()
#clickBoxEvent()----------------------------------------------------
def clickBoxEvent(event):
    #tömmer textfält innan lägger till nytt
    emtyFields()
    
    item = tabell.item(tabell.selection())  # Get the selected item
    values = item['values']  # Get the values of the selected item
     
    if values:
        id, namn, ras = values
        print(f"Clicked: Id={id} Namn={namn}, ras={ras}")
        labelId.config(text=f"{id}")        
        tfNamn.insert(0, namn)
        tfRas.insert(0, ras)
    else:
        print("No item selected")
    
   
#Skapar och lägger till listbox överst i GUI:et
tabell = ttk.Treeview(root, column=("id", "namn", "ras"), show='headings')
tabell.heading("#1", text="ID")
tabell.heading("#2", text="NAMN")
tabell.heading("#3", text="RAS")

# Initialize the last_click_event attribute
#tabell.bind("<Button-1>", clickBoxEvent)#Obs funkar ej, måste vänta på click
tabell.bind("<ButtonRelease-1>", clickBoxEvent)
pTop.add(tabell)

#Uppdaterar listboxen ovan med hundar när man startar programmet
updateListBox()

#Bottom panel-------------------
pBottom = PanedWindow()
pBottom.pack(fill=BOTH, expand=1)

labelId = Label(pBottom, text="")
labelId.grid(row=0, column=0, sticky=W, padx=20, pady=5)

labelNamn = Label(pBottom, text="Namn: ")
labelNamn.grid(row=1, column=0, sticky=W, padx=20, pady=5)
tfNamn = Entry(pBottom)
tfNamn.grid(row=1, column=1, sticky=W, padx=0, pady=5)

labelRas = Label(pBottom, text="Ras: ")
labelRas.grid(row=2, column=0, sticky=W, padx=20, pady=5)
tfRas = Entry(pBottom)
tfRas.grid(row=2, column=1, sticky=W, padx=0, pady=5)

buttonUppdatera = Button(pBottom, text="Uppdatera", command=updateButtonEvent)
buttonUppdatera.grid(row=3, column=0, sticky=W, padx=20, pady=5)

buttonDel = Button(pBottom, text="Tabort hund", command=delButtonEvent)
buttonDel.grid(row=3, column=1, sticky=W, padx=20, pady=5)

buttonClear = Button(pBottom, text="Rensa textfält", command=emtyFields)
buttonClear.grid(row=3, column=2, sticky=W, padx=20, pady=5)

root.mainloop()