import motorcykel
import motorcykelhandler
import motorcykel_app_menu


def main():
    
    
    mc_handler = motorcykelhandler.MotorcykelHandler()

    while True:
        val = motorcykel_app_menu.printMenu()

        if val == "1":
            print("val 1")

        elif val == "2":#lägg till motrcyke
            mc = motorcykel_app_menu.createMotorcykel()
            #print(f"Motorcykel= {mc.fabrikat} modell {mc.modell} kubik {mc.kubik}  TYP {type(mc)}")
            #input("check")
            mc_handler.addMotorcykel(mc)

        elif val == "3":
            print("val 3")
        
        elif val == "4":
            break

        else:
            print("Ogiltig inmatning!")
        




   


    #t_m = motorcykel.Motorcykel(1, "Yamaha", "xy", 400, 300, 56, 220)
    #t_m.getFabrikat()

    #mc_handler.addMotorcykel(t_m)
    
    #Create table körs bara första gången när man skapar tabellen!
    #mc_handler.create_table()
    
    #t_bike = motorcykel.Motorcykel(fa)

main()
