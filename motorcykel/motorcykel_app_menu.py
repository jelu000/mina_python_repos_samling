import os
import motorcykel
from prettytable import PrettyTable
# pip install prettytable
#https://www.javatpoint.com/prettytable-in-python


def printMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n------------------------------------------\n")
    print("\t-MENU- \U0001F603")
    print("\t1. Lista motorcyklar")
    print("\t2. Läggtill motorcykel")
    print("\t3. Tabort motorcykel")
    print("\t4. Avsluta")
    
    val = input("\n\tMata in val: ")
    return val

#return Motorcykel
def createMotorcykel():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n------------------------------------------")
    fabrikat = input("\n\tMata in fabrikat: ")
    modell = input("\n\tMata in modell: ")
    kubik = int(input("\n\tMata in kubik: "))
    vikt = int(input("\n\tMata in vikt: "))
    hk = int(input("\n\tMata in hk: "))
    topphastighet = int(input("\n\tMata in topphastighet: "))

    return   motorcykel.Motorcykel(None, fabrikat, modell, kubik, vikt, hk, topphastighet)
#List all motorcykles
def printListMotorcykel(list_motorcyklar):
    os.system('cls' if os.name == 'nt' else 'clear')
    t_table = PrettyTable(['Id', 'Fabrikat', 'Modell', 'Kubik', 'Vikt', 'Hk', 'Topphastighet'])

    for mc in list_motorcyklar:
        t_table.add_row([mc.id, mc.fabrikat, mc.modell, mc.kubik, mc.vikt, mc.hk, mc.topphastighet])
    
    print(t_table)
    input("Fortsätta? tryck Enter: ")


def printDeleteMotorcykel():
    os.system('cls' if os.name == 'nt' else 'clear')
    return input("\tMata in id på motorcykel som ska tas bort: ")