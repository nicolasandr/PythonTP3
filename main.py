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
    print("4_ Buscar patente")

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
        # consultamos el pais del que proviene el vehiculo
        pais_vehiculo = pais_de_vehiculo(arreglo_registros[i].patente)
        # iprimimos cada fila con el nombre del pais de cabina
        print(arreglo_registros[i], ":", pais_vehiculo)


def pais_cabina(pais):
    pais_de_cabina = 0
    # Cargamos el importe base en funcion de encuentra ubicada la cabina de peaje:
    if pais == "0":
        # Argentina
        pais_de_cabina = "Argentina"
    if pais == "1":
        # Bolivia
        pais_de_cabina = "Bolivia"
    if pais == "2":
        # Brasil
        pais_de_cabina = "Brasil"
    if pais == "3":
        # Paraguay
        pais_de_cabina = "Paraguay"
    if pais == "4":
        # Uruguay
        pais_de_cabina = "Uruguay"

    return pais_de_cabina


def forma_de_pago(pago):
    forma_pag = 0

    if pago == "1":
        forma_pag = "manual"
    if pago == "2":
        forma_pag = "Telepeaje"

    return forma_pag


def tipo_vehiculo(vehiculo):
    tipo = 0
    if vehiculo == "0":
        tipo = "Motocicleta"
    if vehiculo == "1":
        tipo = "Automovil"
    if vehiculo == "2":
        tipo = "Camion"

    return tipo


def buscar_patente(arreglo_registros):
    patente_a_buscar = str(patente(mensaje="\nIngrese patente (debe contener 7 digitos o 6 digitos si la patente es "
                                           "chilena): "))
    pais_de_cabina = str(tipo_vehiculo_o_pais_cabina(0, 4, mensaje="\nIngrese donde se encuentra la cabina (0: "
                                                                   "Argentina - 1: Bolivia - 2: Brasil - 3: "
                                                                   "Paraguay - 4: Uruguay): "))
    se_encontro_patente = False

    for i in range(len(arreglo_registros)):
        if arreglo_registros[i].patente == patente_a_buscar and arreglo_registros[i].pais_cabina == pais_de_cabina:
            print("\nPais del vehiculo:", pais_de_vehiculo(arreglo_registros[i].patente))
            print("patente:", arreglo_registros[i].patente)
            print("pais de cabina:", pais_cabina(arreglo_registros[i].pais_cabina))
            print("Kilometros:", arreglo_registros[i].kilometros)
            print("forma de pago:", forma_de_pago(arreglo_registros[i].forma_pago))
            print("tipo de vehiculo:", tipo_vehiculo(arreglo_registros[i].tipo_vehiculo))
            print("Codigo identificacion de ticket:", arreglo_registros[i].id)
            se_encontro_patente = True
            break
    if not se_encontro_patente:
        print(arreglo_registros[1].patente, " ", arreglo_registros[1].pais_cabina)
        print("\nNo existe registro de la patente en el sistema.")


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
        elif opcion == 4:
            buscar_patente(arreglo_registros)


if __name__ == '__main__':
    Principal()
