# coding=
from tkinter import *
import dog
from tkinter import messagebox

dogs_object = dog.Dog()

root = Tk()  # create root window
root.title("Hundar")
root.geometry("800x400")

#Top panel ----------------------
pTop = PanedWindow(background='green')
pTop.pack(fill=BOTH, expand=1)

def updateListBox():

    listbox_dogs.delete(0, END)

    lista_dogs = dogs_object.get_dog_list()

    for dog in lista_dogs:
        listbox_dogs.insert(dog.id,  f"Namn: {dog.namn},   Ras: {dog.ras} ")


def updateButtonEvent():

    hundnamn = tfNamn.get()
    hundras = tfRas.get()
    hundid = tfId.get()
      
    try:
        
        if hundid == "":
            
            list_dogs = dogs_object.add_dog(hundnamn,hundras)
            updateListBox()

        else:
            list_dogs = dogs_object.update_dog(int(hundid), hundnamn, hundras)
    
    except ValueError:
       messagebox.showerror("ERroR!")



listbox_dogs = Listbox(pTop)
#Uppdaterar listboxen med mc
updateListBox()

pTop.add(listbox_dogs)

#Bottom panel-------------------
pBottom = PanedWindow()
pBottom.pack(fill=BOTH, expand=1)


labelId = Label(pBottom, text="Id: ")
labelId.grid(row=0, column=0, sticky=W, padx=20, pady=5)
tfId = Entry(pBottom, state=DISABLED)
tfId.grid(row=0, column=1, sticky=W, padx=0, pady=5)

labelNamn = Label(pBottom, text="Namn: ")
labelNamn.grid(row=1, column=0, sticky=W, padx=20, pady=5)
tfNamn = Entry(pBottom)
tfNamn.grid(row=1, column=1, sticky=W, padx=0, pady=5)

labelRas = Label(pBottom, text="Ras: ")
labelRas.grid(row=2, column=0, sticky=W, padx=20, pady=5)
tfRas = Entry(pBottom)
tfRas.grid(row=2, column=1, sticky=W, padx=0, pady=5)

buttonUppdatera = Button(pBottom, text="Uppdatera", command=updateButtonEvent)
buttonUppdatera.grid(row=6, column=0, sticky=W, padx=20, pady=5)


root.mainloop()