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
    print("3_ leer arreglo")

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
    return arreglo_registros


def cargar_ticket(linea, arreglo_registros):
    id = linea[0:10]
    patent = linea[10:17]
    tipo_vehiculo = linea[17]
    forma_pag = linea[18]
    pais_cabina = linea[19]
    kilomentros = linea[20:23]

    arreglo_registros.append(Ticket(id, patent, tipo_vehiculo, forma_pag, pais_cabina, kilomentros))

    return arreglo_registros


def menor_a_mayor(arr):
    n = len(arr)

    for i in range(n):
        # Encontrar el índice del elemento mínimo en el subarreglo no ordenado
        min_idx = i
        for j in range(i + 1, n):
            if arr[j].id < arr[min_idx].id:
                min_idx = j

        # Intercambiar el elemento mínimo encontrado con el elemento en la posición actual
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def leerarchivo(arreglo_registros):

    menor_a_mayor(arreglo_registros)

    for i in range(len(arreglo_registros)):
        # consultamos el pais de cabina
        pais_de_cabina = pais_cabina(arreglo_registros[i].patente)
        # iprimimos cada fila con el nombre del pais de cabina
        print(arreglo_registros[i], ":", pais_de_cabina)


def Principal():
    opcion = -1
    arreglo_registros = []

    while opcion != 0:
        mostrar_menu()
        opcion = int(input("Ingrese su elección: "))
        if opcion == 1:
            if len(arreglo_registros):
                while True:
                    entrada = int(input("esta seguro que desea eliminar el arreglo? (1 = Aceptar / 2 = Cancelar): "))
                    if entrada == 1 or entrada == 2:
                        if entrada == 1:
                            arreglo_registros.clear()
                            break
                        if entrada == 2:
                            break
                    else:
                        print("Debes ingresar un valor numérico válido entre(1 y 2).")
            else:
                arreglo_registros = crear_arreglo()

        elif opcion == 2:
            vector_nuevo_ticket = nuevo_ticket()
            mi_lista = ''.join(vector_nuevo_ticket)
            cargar_ticket(mi_lista, arreglo_registros)
        elif opcion == 3:
            leerarchivo(arreglo_registros)


if __name__ == '__main__':
    Principal()
