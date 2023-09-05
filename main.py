from funciones import *


def lenguaje(linea_1):
    idioma = 0
    if "PT" in linea_1:
        idioma = "Portugués"
    if "ES" in linea_1:
        idioma = "Español"
    return idioma


def mostrar_menu():
    print("\nMENU PRINCIPAL:")
    print("\n1_ Crear arreglo de registros")
    print("2_ Cargar por teclado los datos de un ticket")
    print("0_ Para finalizar\n")


def crear_arreglo():
    file = open("peajes-tp3.txt", "rt")
    linea = file.readline().upper()
    idioma = lenguaje(linea)
    arreglo_registros = []

    while True:
        linea = file.readline().upper()
        if linea == "" or linea == "\n":
            break

        id = linea[0:10]
        patent = linea[10:17]
        tipo_vehiculo = linea[17]
        forma_pag = linea[18]
        pais_cabina = linea[19]
        kilomentros = linea[20:23]

        arreglo_registros.append(Ticket(id, patent, tipo_vehiculo, forma_pag, pais_cabina, kilomentros))

    file.close()


def cargar_ticket(linea):
    id = linea[0:10]
    patent = linea[10:17]
    tipo_vehiculo = linea[17]
    forma_pag = linea[18]
    pais_cabina = linea[19]
    kilomentros = linea[20:23]

    linea_nueva = str(Ticket(id, patent, tipo_vehiculo, forma_pag, pais_cabina, kilomentros))

    with open("peajes-tp3.txt", "a") as file:
        file.write(linea_nueva + "\n")


def leerarchivo():
    file = open("peajes-tp3.txt", "rt")
    for i in file:
        print(i)
    file.close()


def Principal():
    opcion = -1

    while opcion != 0:
        mostrar_menu()
        opcion = int(input("Ingrese su elección: "))
        if opcion == 1:
            crear_arreglo()
        elif opcion == 2:
            vector_nuevo_ticket = nuevo_ticket()
            mi_lista = ''.join(vector_nuevo_ticket)
            cargar_ticket(mi_lista)
        elif opcion == 3:
            leerarchivo()


if __name__ == '__main__':
    Principal()
