import dispositivos

opciones_bucle = 0
opcion_menu = ""

while opciones_bucle != 5:
    print("******************************* \n*       SmartHome Menu        *")
    print("1. Agregar dispositivo")
    print("2. Listar dispositivos")
    print("3. Buscar dispositivo")
    print("4. Borrar dispositivo")
    print("5. Salir")
    print("                                                          ")

    opcion_menu = input("Seleccione una opción (1-5): ")

    match opcion_menu:
        case "1":
            tipo_dispositivo = input("Ingrese el tipo de dispositivo: ")
            nombre_dispositivo = input("Ingrese el nombre del dispositivo: ")
            dispositivos.crear_dispositivo(tipo_dispositivo, nombre_dispositivo)
            pass

        case "2":
            dispositivos.listar_dispositivos()
            pass

        case "3":
            nombre_dispositivo = input("Ingrese el nombre del dispositivo a buscar: ")
            dispositivos.buscar_dispositivo_por_nombre(nombre_dispositivo)
            pass

        case "4":
            nombre_dispositivo = input("Ingrese el nombre del dispositivo a eliminar: ")
            dispositivos.eliminar_dispositivo_por_nombre(nombre_dispositivo)
            pass

        case "5":
            print("Finalizando Aplicacion")
            pass
        
        case _:
            print("Opcion invalida")