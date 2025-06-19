
def buscar_contacto():
    if len(contactos) == 0:
        print ("No hay contacto registrado")
    else:
        busqueda = input("Ingrese la informacion del contacto a buscar:\n")
        encontrados = []
        for contacto in contactos:
            if busqueda in contacto.lower():
                encontrados.append(contacto)
        if len(encontrados) > 0:
            print ("Contacto")
            for i in range(len(encontrados)):
                print (f"{i+1}. {contactos[i]} - Tel: {telefonos[i]} - Email: {emails[i]}")

def eliminar_contacto():
    nombre_buscado = input("Ingresa el nombre del contacto a eliminar.")
    if nombre_buscado in contactos:
        indice = contactos.index(nombre_buscado)
        del contactos[indice]
        del telefonos[indice]
        del emails[indice]
        print (f"Contacto {nombre_buscado} Eliminado correctamente.")
    else:
        print (f"No se encontro el contacto: {nombre_buscado}")

contactos = []
telefonos = []
emails = []
def agregar_contacto ():
    
    nombre = input("Ingrese nombre:")
    contactos.append(nombre)
    telefono = input("Ingrese telefono:")
    telefonos.append(telefono)
    email = input("Ingrese mail:")
    emails.append(email)
    print(f"El contacto a sido registrado.\n{nombre, telefono, email}")

def mostrar_contacto ():
    if len(contactos) == 0:
        print("No hay contactos registrados.")
    else:
        for i in range(len(contactos)):
            print(f"{i+1}. {contactos[i]} - Tel: {telefonos[i]} - Email: {emails[i]}")

