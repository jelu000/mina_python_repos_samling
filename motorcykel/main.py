import motorcykel
import motorcykelhandler
import motorcykel_app_menu


def main():
    
    
    mc_handler = motorcykelhandler.MotorcykelHandler()

    while True:
        val = motorcykel_app_menu.printMenu()

        if val == "1":#Lista Motorcyklar

            lista_motorcyklar = mc_handler.readSqliteTable()
            mc = motorcykel_app_menu.printListMotorcykel(lista_motorcyklar)
            
        elif val == "2":#lägg till motrcyke
            mc = motorcykel_app_menu.createMotorcykel()
            #print(f"Motorcykel= {mc.fabrikat} modell {mc.modell} kubik {mc.kubik}  TYP {type(mc)}")
            mc_handler.addMotorcykel(mc)

        elif val == "3":#Tabort motorcykel
            t_id =  motorcykel_app_menu.printDeleteMotorcykel()
            mc_handler.deleteMotorcykel(t_id)
            input("\tFortsätta? tryck Enter: ")
        
        elif val == "4":#Avsluta
            break

        else:
            print("Ogiltig inmatning!")
          

main()
