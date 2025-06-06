#csawdwd
# BLIOTECA DE LIBLOS ctl+k+s
import os
import json
# historial con las historiales eliminanos 


contactos = {
    "contacto" : []
}
contador = 0

lista_Contactos = []

def leerJson(path: str):
    with open(path, mode='r') as file:
        datos = json.load(file)
        return datos
    
def escribirJson(path: str, data: list):
    with open(path,mode= 'w') as file:
        json.dump(data, file, indent= 4)

def clear_screen():
    # Función para limpiar la pantalla
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux/Unix
        
def espacio():
    print("\n" * 1)

def validacion_ingreso(mensaje: str, valorminimo: int = 0, valormaximo: int = 6):
    while True:
        try:
            valor = int(input(mensaje))
            if valorminimo <= valor <= valormaximo:
                return valor
            else:
                print(f"POR FAVOR INGRESE VALORES ENTRE {valorminimo} y {valormaximo}.")
        except:
            print("Entrada no válida. Por favor, ingrese un número entero.")

def rango_clear_screen(variable: int, valorminimo: int, valormaximo: int):
    if valorminimo <= variable <= valormaximo:
        clear_screen()

def validar_texto(mensaje: str):
    # Función para validar el ingreso de texto
    while True:
        valor = input(mensaje)
        suplente = valor.replace(" ", "")
        if suplente.isalpha() == True :
            valor = valor.upper()
            return valor
            break
        else:
            print("Entrada no válida. Por favor, ingrese solo texto (letras).")
            continue
            # Aquí podrías agregar una validación para que el texto comience con mayúscula si es necesario

def Menu_principal():
    print("CRUD DE JSON")
    print("1. CREAR CONTACTO")
    print("2. ACTUALIZAR CONTACTO")
    print("3. LEER LOS CONTACTOS")
    print("4. ELIMINAR CONTACTOS")
    print("=====================================")
    espacio()

def Validar_menu(mensaje: str, valorminimo: int, valormaximo: int):
    while True:
        try:
            valor = int(input(mensaje))
            if valorminimo <= valor <= valormaximo:
                return valor
            else:
                print(f"POR FAVOR INGRESE VALORES ENTRE {valorminimo} y {valormaximo}.")
                espacio()
                Menu_principal()
        except:
            print("ENTRADA NO VALIDAD POR FAVOR")
            Menu_principal()

def Crear_Contacto(id: int, nombre: str, telefono: int, email: str):
    return {
        "id": id,
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }

def ingresar_Contacto(contacto: dict, ingreso = list):
    # Función para ingresar un libro 
    espacio()
    contacto = Crear_Contacto(
        id = validacion_ingreso(f"INGRESE LA IDENTIFIACION DEL USUARIO  \n ", 4000000, 20000000000),
        nombre= validar_texto(f"INGRESE EL NOMBRE DEL CONTACTO  \n"),
        telefono= validacion_ingreso(f"TELEFONO DEL CONTACTO \n",1000000000,200000000000),
        email= input("INGRESE EL CORREO ELECTRONICO \n")
    )
    ingreso.append(contacto)

def actualizarJSON(ingreso: str):

    opcion = validacion_ingreso("Ingrese el ID del usuario a modificar: ", 4000000, 2000000000)
    try:
        ingresos = leerJson(ingreso)
        espacio()
        for contacto in ingresos:
            if contacto["id"] == opcion:
                contacto["nombre"] = validar_texto(f"Ingrese el nuevo nombre:  \n")
                contacto["telefono"] = validacion_ingreso(f"Ingrese el nuevo telefono:  \n",1000000000,20000000000)
                contacto["email"] = validar_texto(f"Ingrese el nuevo email:  \n")
                escribirJson("Contactos.json",ingresos)
                print("ACTUALIZACION EXITOSA")

                espacio()
            else:
                print(f"No se encontró el usuario con ID {opcion}.")
        # ingresos.append(contacto)
        # escribirJson("Contacto.json",ingresos)
    except:
        print(f"No se encontró el usuario con ID {opcion}.")

def Alistar(ingreso: str):
     try:
        contactos = leerJson(ingreso)
        if contactos:
            print("LISTA DE CONTACTOS:")
            for contacto in contactos:
                print(f"SU IDENTIFICACION ES: {contacto['id']}\nSU NOMBRE ES: {contacto['nombre']} \nSU TELEFONO ES: {contacto['telefono']} \nSU CORREO ES: {contacto['email']} \n")
        else:
            print("No hay contactos registrados.")
     except:
        print(f"El archivo {ingreso} no existe.")
    

def eliminar_contacto_por_id(path: str):
    try:
        contactos = leerJson(path)
        id_eliminar = validacion_ingreso("Ingrese la identificación del contacto a eliminar: ", 4000000, 20000000000)
        for contacto in contactos:
            if contacto["id"] == id_eliminar:
                contactos.remove(contacto)
                escribirJson(path, contactos)
                print(f"Contacto con ID {id_eliminar} eliminado exitosamente.")
                break
        
    except:
        print("NO ESTA EN LA BASE DE DATOS")

while True :
    Menu_principal()
    opcion = Validar_menu("INGRESE UNA OPCION \n",0,4)
    espacio()
    rango_clear_screen(opcion, 0, 4)

    if opcion == 1:
        ingresar_Contacto(contactos,lista_Contactos)
        escribirJson("Contactos.json", lista_Contactos)

    elif opcion ==2:
        actualizarJSON("Contactos.json")

    elif opcion == 3:
        Alistar("Contactos.json")
    
    elif opcion == 4:
        eliminar_contacto_por_id("Contactos.json")

        pass

    elif opcion == 0:
        break
        