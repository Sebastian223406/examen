import os
import json
item=[]
items=[]
def limpiarConsola():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
MenuOptions = """

        ==========🤑 MENÚ DE TABLEROS 🤑========== 
    1️⃣  GESTION DE TABLEROS
    2️⃣  GESTION DE LISTAS
    3️⃣  GESTION DE TARJETAS
    4️⃣  PERSISTENCIA DE DATOS

"""
subMenoOptions1 = """

    MENU - GESTION DE TABLEROS
    
    1)  Crear un nuevo Tablero
    2)  Ver todas los Tableros
    3)  Actualizar el nombre de un Tablero
    4)  Eliminar un Tablero

"""
Lista = {
    "": [],
    "": [],
    "": [],
}




def eliminarUtiles():
    itemPosicion = int(input("Ingrese la posicion del Util Inutil: \n")) - 1
    itemEliminado = item.pop(itemPosicion)
    print(f"El Util Inutil elimado fue: {itemEliminado[0]}")
while True:
        limpiarConsola()
        opcion = input("🔢 Selecciona una opción: ")

        if opcion == "1":
            print (subMenoOptions1)
            
            opcion2 = input("🔢 Selecciona una opción: ")
        def agregarTableros():
                nombre = input("Ingrese el nombre del Tablero: \n")
                cantidad = int(input(f"Ingrese la cantidad de {nombre} :\n"))
                item.append(nombre)
                item.append(cantidad)
                items.append(item.copy())
                print(items)
                item.clear()
                
        agregarTableros()
        limpiarConsola()

        def mostrarlostableros(tableros):
                     for index,  in enumerate(tableros):
                                 print(f"{index + 1} - Nombre: {item[0]}  Cantidad: {item[1]}")

        if opcion =="2":
            
               entrada = input("📝 ¿Cuántas listas desea tener? (solo hay del 1 al 30): ")
          

 
            
            #with open ("historial_tablero.json", mode = "w") as file:
               #     contenido = file.write()
              #      file.writeline()
             #       file.readlines()
             #       print (file.readline())
            #        print (file.readlines())


               # print ("""
################################################################
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#                                                              #
#############################################################
    #print ("""
######################################################################################
#                                                                                    # 
#                           ,.--------._                                             #
#                           /            ''.                                         #
#                         ,'                \     |"\                /\          /\  #
#                /"|     /                   \    |__"              ( \\        // ) #
#               "_"|    /           z#####z   \  //                  \ \\      // /  #
#                 \\  #####        ##------".  \//                    \_\\||||//_/   #
#                  \\/-----\     /          ".  \                      \/ _  _ \     #
#                   \|      \   |   ,,--..       \                    \/|(O)(O)|     #
#                   | ,.--._ \  (  | ##   \)      \                  \/ |      |     #
#                   |(  ##  )/   \ `-....-//       |///////////////_\/  \      /     #
#                     '--'."      \                \              //     |____|      #
#                  /'    /         ) --.            \            ||     /      \     #
#               ,..|     \.________/    `-..         \   \       \|     \ 0  0 /     #
#            _,##/ |   ,/   /   \           \         \   \       U    / \_//_/      #
#          :###.-  |  ,/   /     \        /' ""\      .\        (     /              #
#         /####|   |   (.___________,---',/    |       |\=._____|  |_/               #
#        /#####|   |     \__|__|__|__|_,/             |####\    |  ||                #
#       /######\   \      \__________/                /#####|   \  ||                #
#      /|#######`. `\                                /#######\   | ||                #
#     /++\#########\  \                      _,'    _/#########\ | ||                #
#    /++++|#########|  \      .---..       ,/      ,'##########.\|_||                #
#   //++++|#########\.  \.              ,-/      ,'########,+++++\\_\\               #
#  /++++++|##########\.   '._        _,/       ,'######,''++++++++\                  #
# |+++++++|###########|       -----."        _'#######' +++++++++++\                 #
# |+++++++|############\.     \\     //      /#######/++++ S@yaN +++\                #
#      ________________________\\___//______________________________________         #
#  ____                    _           _         _                                   #
#         / ___| __ _ _   _    ___| |   __ _  | | ___   | | ___  __ _                #
#        | |  _ / _` | | | |  / _ \ |  / _` | | |/ _ \  | |/ _ \/ _` |               #
#        | |_| | (_| | |_| | |  __/ | | (_| | | | (_) | | |  __/ (_| |               #
#         \____|\__,_|\__, |  \___|_|  \__, | |_|\___/  |_|\___|\__,_|               #
#             |___/               |_|                                                #
######################################################################################