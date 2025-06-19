import os
from functions import *

#Bienvenida
print("Bienvenido a la plataforma de registro de contactos.")
#Menú principal y opciones.
opcion = 0
while opcion != 5:
    print("1.- Agregar contacto.\n2.- Listar contactos.\
        \n 3.- Buscar un contacto por nombre.\n 4.- Eliminar un contacto. \n\
            5.- Salir del programa")
    try:
        opcion = int(input("Selecciona una opción para continuar"))
    except:
        print("Las opciones son numéricas.")
    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        print("Gracias por utilizar el programa!")
    else:
        print("Debes elegir una opción válida")