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