from tkinter import *
import motorcykelhandler
import motorcykel
from tkinter import messagebox

mc_handler = motorcykelhandler.MotorcykelHandler()

root = Tk()  # create root window
root.title("Motorcyklar")
root.config(bg="red")

# Create Frame widget
#outer_frame = Frame(root, width=800, height=800)
#outer_frame.grid(row=0, column=0, padx=10, pady=5)

root.geometry("800x600")


#Top panel ----------------------
pTop = PanedWindow(background='green')
pTop.pack(fill=BOTH, expand=1)


def updateListBox():

    listboxMc.delete(0, END)

    lista_mc = mc_handler.readSqliteTable()

    for i, mc in  enumerate(lista_mc):
        listboxMc.insert(i, f"{mc.fabrikat} {mc.modell}:    Kubik: {mc.kubik}, Vikt: {mc.vikt}, HK: {mc.hk}, Topphastighet: {mc.topphastighet}")
    #listboxMc.insert(1, "Hej")


def updateButtonEvent():

    t_mc = motorcykel.Motorcykel(None, tfFabrikat.get(), tfModell.get(), int(tfKubik.get()), int(tfVikt.get()), int(tfHk.get()), int(tfHastighet.get()))
    
    try:
        
        if tfFabrikat.get() != "" or tfModell.get() != "":
            mc_handler.addMotorcykel(t_mc)

            updateListBox()

        else:
            messagebox.showinfo("Måste fylla i fabrikat och modell")
    
    except ValueError:
        messagebox.showerror("ERroR!")




listboxMc = Listbox(pTop)
#Uppdaterar listboxen med mc

updateListBox()

pTop.add(listboxMc)

#Bottom panel-------------------
pBottom = PanedWindow()
pBottom.pack(fill=BOTH, expand=1)

#Lägger till titlar och textfällt
labelFabrikat = Label(pBottom, text="Fabrikat: ")
labelFabrikat.grid(row=0, column=0, sticky=W, padx=20, pady=5)
tfFabrikat = Entry(pBottom)
tfFabrikat.grid(row=0, column=1, sticky=W, padx=0, pady=5)

labelModell = Label(pBottom, text="Modell: ")
labelModell.grid(row=1, column=0, sticky=W, padx=20, pady=5)
tfModell = Entry(pBottom)
tfModell.grid(row=1, column=1, sticky=W, padx=0, pady=5)

labelKubik = Label(pBottom, text="Kubik: ")
labelKubik.grid(row=2, column=0, sticky=W, padx=20, pady=5)
tfKubik = Entry(pBottom)
tfKubik.grid(row=2, column=1, sticky=W, padx=0, pady=5)

labelVikt = Label(pBottom, text="Vikt: ")
labelVikt.grid(row=3, column=0, sticky=W, padx=20, pady=5)
tfVikt = Entry(pBottom)
tfVikt.grid(row=3, column=1, sticky=W, padx=0, pady=5)

labelHk = Label(pBottom, text="Hk: ")
labelHk.grid(row=4, column=0, sticky=W, padx=20, pady=5)
tfHk = Entry(pBottom)
tfHk.grid(row=4, column=1, sticky=W, padx=0, pady=5)

labelHastighet = Label(pBottom, text="Topphastighet: ")
labelHastighet.grid(row=5, column=0, sticky=W, padx=20, pady=5)
tfHastighet = Entry(pBottom)
tfHastighet.grid(row=5, column=1, sticky=W, padx=0, pady=5)

buttonUppdatera = Button(pBottom, text="Uppdatera", command=updateButtonEvent)
buttonUppdatera.grid(row=6, column=0, sticky=W, padx=20, pady=5)




    




root.mainloop()