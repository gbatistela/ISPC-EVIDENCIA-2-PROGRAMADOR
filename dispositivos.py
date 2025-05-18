from datetime import datetime

dispositivos = []

id_dispositivo = 1


def crear_dispositivo(tipo_dispositivo, nombre_dispositivo):
    global id_dispositivo

    nuevo_dispositivo = {
        "Id": id_dispositivo,
        "Tipo Dispositivo": tipo_dispositivo,
        "Nombre Dispositivo": nombre_dispositivo,
        "Estado": False, 
        "Fecha de Creacion": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    dispositivos.append(nuevo_dispositivo)
    id_dispositivo += 1

    return nuevo_dispositivo


def buscar_dispositivo_por_nombre(nombre_dispositivo):
    for i in dispositivos:
        if i["Nombre Dispositivo"] == nombre_dispositivo:
            return print(i)

    return print(f"No se encontro el dispositivo: {nombre_dispositivo}")


def listar_dispositivos():
    for i in dispositivos:
        return print(i)
    return print("No se ha encontrado ningun dispositivo")


def eliminar_dispositivo_por_nombre(nombre_dispositivo):
    for i in dispositivos:
        if i["Nombre Dispositivo"] == nombre_dispositivo:
            dispositivos.remove(i)
            return print(f"El dispositivo: {i["Nombre Dispositivo"]}, ha sido eliminado")

    return print(f"No se encontro el dispositivo: {nombre_dispositivo}")


def automatizacion_encender_luces():
    print("movimiento detectado en entrada principal")

    for i in dispositivos:
        if i["Nombre Dispositivo"] == "luces".lower() and i["Estado"] == False:
            i["Estado"] = True
            return print("luces entrada principal encendidas")
            

    return print("No se han detectado luces a encender")    
