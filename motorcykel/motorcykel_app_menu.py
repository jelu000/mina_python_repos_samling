import os
import motorcykel


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