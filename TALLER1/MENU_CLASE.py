#csawdwd
# BLIOTECA DE LIBLOS ctl+k+s
import os
import json
# historial con las historiales eliminanos 


contactos = {
    "contacto" : []
}

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
        id = validacion_ingreso(f"INGRESE LA IDENTIFIACION DEL USUARIO  \n ", 4000000, 2000000000),
        nombre= validar_texto(f"INGRESE EL NOMBRE DEL CONTACTO  \n"),
        telefono= validacion_ingreso(f"TELEFONO DEL CONTACTO \n",1000000000,20000000000),
        email= input("INGRESE EL CORREO ELECTRONICO \n")
    )
    ingreso.append(contacto)

def actualizarJSON(ingreso: str,  recorrido = list):

    opcion = validacion_ingreso("Ingrese el ID del usuario a modificar: ", 4000000, 2000000000)
    try:
        recorrido = leerJson(ingreso)
        espacio()
        for contacto in recorrido:
            if contacto["id"] == opcion:
                contacto["nombre"] = validar_texto(f"Ingrese el nuevo nombre:  \n")
                contacto["telefono"] = validacion_ingreso(f"Ingrese el nuevo telefono:  \n",1000000000,20000000000)
                contacto["email"] = validar_texto(f"Ingrese el nuevo email:  \n")
                print("ACTUALIZACION EXITOSA")
                espacio()
            else:
                print(f"No se encontró el usuario con ID {opcion}.")
        escribirJson("Contactos.json", lista_Contactos)
    except FileNotFoundError as e:
        print(f"El archivo {ingreso} no existe. Por favor, verifique la ruta.\nError: {e}")
    

while True :
    Menu_principal()
    opcion = Validar_menu("INGRESE UNA OPCION \n",0,4)
    espacio()
    rango_clear_screen(opcion, 0, 4)

    if opcion == 1:
        ingresar_Contacto(contactos,lista_Contactos)
        escribirJson("Contactos.json", lista_Contactos)

    elif opcion ==2:
        actualizarJSON("Contactos.json",lista_Contactos)

        pass

    elif opcion == 3:
        pass
    
    elif opcion == 4:
        pass

    elif opcion == 0:
        break
        pass
    pass

# def nuevolibro(codigo: int, titulo: str, autor: str, editorial: str):
#     # Función para crear un nuevo libro
#     return {
#         "codigo": codigo,
#         "titulo": titulo,
#         "autor": autor,
#         "editorial": editorial
#     }

# def ingresar_libro(ingrese = list, mayor = dict):
#     # Función para ingresar un libro 
#     listar_libros()
#     espacio()
#     libro = nuevolibro(
#         codigo= validacion_ingreso(f"Ingrese el código del libro: \n ", 1, 100000),
#         titulo= validar_texto(f"Ingrese el título del libro:  \n"),
#         autor= validar_texto(f"Ingrese el autor del libro:  \n"),
#         editorial= validar_texto(f"Ingrese la editorial del libro:  \n")
#     )
#     mayor["libros"].append(libro)

# def buscar_codigo(archivo_mayor= dict,codigo_libro = int):
#     espacio()
#     bandera = True
#     while bandera:
#         codigo_libro = validacion_ingreso(f"Ingrese el código del libro a buscar: \n", 1, 100000)
#         for libro in archivo_mayor["libros"]:
#             if libro["codigo"] == codigo_libro:
#                 print(f"Libro encontrado: su codigo es:  {libro['codigo']} su nombre es: {libro['titulo']}")
#                 espacio()
#                 codigo_libro = libro["codigo"]
#                 bandera = False
#                 print(codigo_libro)
#                 return codigo_libro
#                 break
#         if bandera:
#             print(f"No se encontró un libro con el código {codigo_libro}.")
#             espacio()
#             continue

# def buscar_codigo_prestamo(archivo_mayor= dict, codigo_libro = int):
#     espacio()
#     bandera = True
#     while bandera:
#         codigo_libro = validacion_ingreso(f"Ingrese el código del libro a buscar: \n", 1, 100000)
#         for libro in archivo_mayor["prestamos"]:
#             if libro["codigo_libro"] == codigo_libro:
#                 print(f"Libro encontrado: su codigo es:  {libro['codigo_libro']} su nombre es: {libro['nombrelibro']}")
#                 espacio()
#                 codigo_libro = libro["codigo_libro"]
#                 bandera = False
#                 print(codigo_libro)
#                 return codigo_libro
#                 break
#         if bandera:
#             print(f"No se encontró un libro con el código {codigo_libro}.")
#             espacio()
#             continue

# def actualizar_libro(archivo_mayor= dict, ):
#     espacio()
#     listar_libros()
#     buscar_codigo(archivo_mayor, codigo_libro)
#     espacio()
#     for libro in archivo_mayor["libros"]:
#         libro["titulo"] = validar_texto(f"Ingrese el nuevo título del libro:  \n")
#         libro["autor"] = validar_texto(f"Ingrese el nuevo autor del libro:  \n")
#         libro["editorial"] = validar_texto(f"Ingrese la nueva editorial del libro:  \n")
#         print("Libro actualizado exitosamente.")
#         espacio()
#         return
#     espacio()
#     return

# def archivo_libros_eliminados(codigo: int, titulo: str, autor: str, editorial: str):
#     return {
#         "codigo_eliminado": codigo,
#         "titulo_eliminado": titulo,
#         "autor_eliminado": autor,
#         "editorial_eliminado": editorial
#     }   


# def eliminar_libro(archivo_mayor = dict,):
#     espacio()
#     listar_libros()
#     codigo_libro = validacion_ingreso(f"Ingrese el código del libro a eliminar: \n", 1, 100000)
#     bandera = True
#     while bandera:
#         for libro in biblioteca["libros"]:
#             if libro["codigo"] == codigo_libro:
#                 codigo1 = libro["codigo"]
#                 titulo1 = libro["titulo"]
#                 autor1 = libro["autor"]
#                 editorial1 = libro["editorial"]
#                 archivo_mayor["libros"].remove(libro)
#                 print(f"Libro con código {codigo_libro} eliminado exitosamente.")
#                 espacio()
#                 bandera = False
#             else:
#                 print(f"No se encontró un libro con el código {codigo_libro}.")
#                 espacio()

#     libro_eliminado = archivo_libros_eliminados(
#                 codigo= codigo1,
#                 titulo=titulo1,
#                 autor=autor1,
#                 editorial=editorial1
#             )
#     print(libro_eliminado)
    
#     archivo_mayor["libros_eliminados"].append(libro_eliminado)
#     espacio()
# def lista_libros_eliminados():

#     if biblioteca["libros_eliminados"]:
#         for libro in biblioteca["libros_eliminados"]:
#             print(f"Código: {libro['codigo_eliminado']}, Título: {libro['titulo_eliminado']}, Autor: {libro['autor_eliminado']}, Editorial: {libro['editorial_eliminado']}")
#     else:
#         print("No hay libros en la biblioteca.")

    
# def nuevo_prestamo(cedula: int, usuario: str,nombrelibro: str,codigo_librop: int):
#     # Función para crear un nuevo préstamo
#     return {
#         "cedula": cedula,
#         "nombreusuario": usuario,
#         "codigo_libro": codigo_librop,
#         "nombrelibro": nombrelibro
#     }

# def archivar_prestamos(ingrese = list, mayor = dict):
#     listar_libros()
#     codigoaux = validacion_ingreso(f"Ingrese el código del libro a prestar: \n", 1, 100000)

#     for libro in mayor["prestamos"]:
#         if libro["codigo_libro"] == codigoaux:
#             espacio()
#             print(f"El libro con código {codigoaux} ya está prestado.")
#             espacio()
#             return
#     for libro in mayor["libros"]:
#         if libro["codigo"] == codigoaux:
#             print(f"Libro encontrado: su codigo es:  {libro['codigo']} su nombre es: {libro['titulo']}")
#             espacio()
#             codigolibro = libro["codigo"]
#             nombrelibro = libro["titulo"]
#             break
#     else:
#         print(f"No se encontró un libro con el código {codigoaux}.")
#         espacio()
#         return
    

#     prestamo = nuevo_prestamo (
#         usuario = validar_texto(f"Ingrese su nombre de usuario: \n"),
#         cedula = validacion_ingreso(f"Ingrese su cédula: \n", 10000000, 2000000000),
#         nombrelibro = nombrelibro,
#         codigo_librop = codigolibro
#     )

    
#     espacio()
#     mayor["prestamos"].append(prestamo)

# def listar_libros():
#     # Función para listar los libros
#     if biblioteca["libros"]:
#         print("LISTA DE LIBROS:")
#         for libro in biblioteca["libros"]:
#             print(f"Código: {libro['codigo']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Editorial: {libro['editorial']}")
#     else:
#         print("No hay libros en la biblioteca.")
    
# def listar_prestamos():

#     # Función para listar los préstamos
#     if biblioteca["prestamos"]:
#         print("LISTA DE PRÉSTAMOS:")
#         for prestamo in biblioteca["prestamos"]:
#             print(f"Cédula: {prestamo['cedula']}, Usuario: {prestamo['nombreusuario']}, Código del Libro: {prestamo['codigo_libro']}, Nombre del Libro: {prestamo['nombrelibro']}")
#     else:
#         print("No hay préstamos registrados.")

# def eliminar_prestamo(mayor = dict, codigo_libro = int):

#     for prestamo in mayor["prestamos"]:
#         if prestamo["codigo_libro"] == codigo_libro:
#             mayor["prestamos"].remove(prestamo)
#             espacio()
#             return
    
# def preparar_devolucion(codigo_libro: int, nombrelibro: str, cedula: int, nombreusuario: str):
#     return {
#         "codigo_libro": codigo_libro,
#         "nombrelibro": nombrelibro, 
#         "cedula": cedula,
#         "nombreusuario": nombreusuario
#     }

# def archivar_devoluciones(lista = list, mayor = dict):
#     codigodevolucion = validacion_ingreso(f"Ingrese el código del libro a devolver: \n", 1, 100000)
#     for libro in biblioteca["prestamos"]:
#         if libro["codigo_libro"] == codigodevolucion:
#             print(f"Libro encontrado: su codigo es:  {libro['codigo_libro']} su nombre es: {libro['nombrelibro']}")
#             espacio()
#             break
#     else:
#         print(f"No se encontró un libro con el código {codigodevolucion}.")
#         espacio()
#         return
#     espacio()
    
#     espacio()
#     for libro in biblioteca["prestamos"]:
#             if libro["codigo_libro"] == codigodevolucion:
#                 codigo_librol = libro["codigo_libro"]
#                 nombrelibrol = libro["nombrelibro"] 
#                 cedulal = libro["cedula"]
#                 nombreusuariol = libro["nombreusuario"]
#     devolucion = preparar_devolucion(
#         codigo_libro=codigo_librol,  
#         nombrelibro=nombrelibrol,
#         cedula=cedulal,
#         nombreusuario=nombreusuariol
#     )
#     mayor["devoluciones"].append(devolucion)
#     espacio()

#     eliminar_prestamo(mayor, codigodevolucion)
#     print("Devolución registrada exitosamente.")
    
# def listar_devoluciones():
#     # Función para listar las devoluciones
#     if biblioteca["devoluciones"]:
#         print("LISTA DE DEVOLUCIONES:")
#         for devolucion in biblioteca["devoluciones"]:
#             print(f"Código del Libro: {devolucion['codigo_libro']}, Nombre del Libro: {devolucion['nombrelibro']}, Cédula: {devolucion['cedula']}, Usuario: {devolucion['nombreusuario']}")
#     else:
#         print("No hay devoluciones registradas.")
    

# while True:
#     menu_principal()
#     espacio()
#     opcion = validacion_ingreso_menu_principal(f"ELIGE UNA OPCION:  \n", 0, 7)
#     espacio()
#     rango_clear_screen(opcion, 0, 7)

#     if opcion == 1 : 
#         while True:
#             sub_menu()
#             espacio()
#             sub_opcion1 = validacion_ingreso_sub_menu_principal(f"ELIGE UNA OPCION:  \n", 0, 4)
#             espacio()
#             rango_clear_screen(sub_opcion1, 0, 4)

#             if sub_opcion1 == 1:
#                 print("AÑADIENDO LIBRO...")
#                 ingresar_libro(libro,biblioteca)
#                 print("LIBRO AÑADIDO EXITOSAMENTE.")
#                 espacio()
#             elif sub_opcion1 == 2:
#                 print("ACTUALIZANDO LIBRO...")
#                 actualizar_libro(biblioteca)
#                 espacio()

#             elif sub_opcion1 == 3 :
#                 print("ELIMINANDO LIBRO...")
#                 eliminar_libro(biblioteca)
#                 espacio()

#             elif sub_opcion1 == 4 :
#                 print("LISTANDO LIBROS...")
#                 espacio()
#                 listar_libros()
#                 espacio()

#             elif sub_opcion1 == 0:
#                 print("VOLVIENDO AL MENÚ PRINCIPAL...")
#                 espacio()
#                 break 
#     elif opcion == 2:
#         print("PRESTAMO DE LIBROS...")
#         archivar_prestamos(prestamo, biblioteca)   
#         espacio()
#     elif opcion == 3:
#         print("DEVOLUCION DE LIBROS...")
#         archivar_devoluciones(devolucion, biblioteca)
#         espacio()

#     elif opcion == 4 :
#         print("LISTAR LIBROS PRESTADOS...")
#         listar_prestamos()
#         espacio()

#     elif opcion == 5 :
#         print("LISTAR LIBROS...")
#         listar_libros()
#         espacio()

#     elif opcion == 6:
#         print("HISTORIAL DE PRESTAMOS Y DEVOLUCIONES ...")
#         espacio()
#         print("AQUI ESTA LOS PRESTAMOS QUE YA FUERON DEVUELTOS ") 
#         listar_devoluciones()
#         espacio()
#         print("AQUI ESTA LOS PRESTAMOS QUE NO HAN SIDO DEVUELTOS")
#         listar_prestamos()
#         espacio()
#     elif opcion == 7:
#         print("LIBROS ELIMINADOS ")
#         print("AQUI ESTA LOS LIBROS QUE HAN SIDO ELIMINADOS")
#         espacio()
#         lista_libros_eliminados()
#         espacio()
#     elif opcion == 0:
#         print("SALIENDO DEL PROGRAMA...")
#         espacio()
#         break
   