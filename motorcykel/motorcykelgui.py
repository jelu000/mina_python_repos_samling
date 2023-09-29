from tkinter import *

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

listboxMc = Listbox(pTop)
listboxMc.insert(1, "Python")
listboxMc.insert(2, "Perl")

pTop.add(listboxMc)

#Bottom panel-------------------
pBottom = PanedWindow()
pBottom.pack(fill=BOTH, expand=1)

#Lägger till titlar och textfällt
labelFabrikat = Label(pBottom, text="Fabrikat: ")
labelFabrikat.grid(row=0, column=0, sticky=W, padx=5, pady=5)
tfFabrikat = Entry(pBottom)
tfFabrikat.grid(row=0, column=1, sticky=W, padx=5, pady=5)

labelModell = Label(pBottom, text="Modell: ")
labelModell.grid(row=1, column=0, sticky=W, padx=5, pady=5)
tfModell = Entry(pBottom)
tfModell.grid(row=1, column=1, sticky=W, padx=5, pady=5)

labelKubik = Label(pBottom, text="Kubik: ")
labelKubik.grid(row=2, column=0, sticky=W, padx=5, pady=5)
tfKubik = Entry(pBottom)
tfKubik.grid(row=2, column=1, sticky=W, padx=5, pady=5)


root.mainloop()