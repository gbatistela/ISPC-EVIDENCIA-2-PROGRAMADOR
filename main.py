import dispositivos

opcion_menu = ""

while True:
    print(" " * 10)     
    print("*******************************")
    print("*                             *")
    print("*       SmartHome Menu        *")
    print("*                             *")
    print("*******************************")
    print("1. Agregar dispositivo")
    print("2. Listar dispositivos")
    print("3. Buscar dispositivo")
    print("4. Borrar dispositivo")
    print("5. Activar Automatizacion")  
    print("6. Salir")  
    print(" " * 10)                                             

    opcion_menu = input("Seleccione una opción (1-6): ")

    match opcion_menu:
        case "1":
            tipo_dispositivo = input("Ingrese el tipo de dispositivo: ").lower()
            nombre_dispositivo = input("Ingrese el nombre del dispositivo: ").lower()
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
            dispositivos.automatizacion_encender_luces()
    
        case "6":
            print("Finalizando Aplicacion")
            break
        
        case _:
            print("Opcion invalida")

        
