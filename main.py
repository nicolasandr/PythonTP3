from funciones import *


def mostrar_menu():
    print(
        "\n"
        "------------------------------------------------------------------------------------------------------------------------------------")
    print("MENU PRINCIPAL:\n(Seleccione una opcion):")
    print("\n\t1_ Crear lista de registros.")
    print("\t2_ Cargar por teclado los datos de un ticket.")
    print("\t3_ Leer lista de registros.")
    print("\t4_ Buscar patente.")
    print("\t5_ Buscar codigo de ticket.")
    print("\t6_ Determinar la cantidad de vehiculos de cada pais que pasaron por las cabinas.")
    print("\t7_ Determinar el total de pagos realizados por cada tipo de vehiculo.")
    print(
        "\t8_ Determinar el mayor monto obtenido del total de pagos realizados de vehiculo,mostrarlo y mostrar el mostrar "
        "porcentaje sobre el total.")
    print("\t9_ Promedio de los kilometros totales recorridos por todos los vehiculos.\n")
    print("\t(Si desea finalizar presione: 0)")
    print(
        "-------------------------------------------------------------------------------------------------------------------------------------\n")


def crear_arreglo():
    file = open("peajes-tp3.txt", "rt")
    timestamp = file.readline()
    arreglo_registros = []

    while True:
        linea = file.readline().upper()
        if linea == "" or linea == "\n":
            break

        id = linea[0:10]
        patent = linea[10:17]
        tipo_vehicul = linea[17]
        forma_pag = linea[18]
        pais_cabin = linea[19]
        kilomentros = linea[20:23]

        arreglo_registros.append(Ticket(id, patent, tipo_vehicul, forma_pag, pais_cabin, kilomentros))

    if arreglo_registros:
        print("\n=====================================================================")
        timestamp_sin_guion_med = timestamp.replace("â€“", "|")
        print("Lista creada correctamente: ", timestamp_sin_guion_med)
    else:
        print("\n================================")
        print("Error no se pudo crear el arreglo")

    file.close()
    return arreglo_registros


def cargar_ticket(linea, arreglo_registros):
    id = linea[0:10]
    patent = linea[10:17]
    tipo_vehicul = linea[17]
    forma_pag = linea[18]
    pais_cabin = linea[19]
    kilomentros = linea[20:23]

    arreglo_registros.append(Ticket(id, patent, tipo_vehicul, forma_pag, pais_cabin, kilomentros))

    print("\n--------------------------")
    print("Registro creado con exito!")

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
        # consultamos el pais del que proviene el vehiculo (retorna numero)
        pais = ["Argentina", "Brasil", "Chile", "Bolivia", "Paraguay", "Uruguay", "Otro"]
        pais_vehiculo = pais_de_vehiculo(arreglo_registros[i].patente)
        # iprimimos cada fila con el nombre del pais de cabina
        print(arreglo_registros[i], "\t\tPais_de_patente:", pais[pais_vehiculo])


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
    pais = ["Argentina", "Brasil", "Chile", "Bolivia", "Paraguay", "Uruguay", "Otro"]
    patente_a_buscar = str(patente(mensaje="\nIngrese patente (debe contener 7 digitos o 6 digitos si la patente es "
                                           "chilena): "))
    pais_de_cabina = str(validacion_entrada(0, 4, mensaje="\nIngrese donde se encuentra la cabina (0: "
                                                          "Argentina - 1: Bolivia - 2: Brasil - 3: "
                                                          "Paraguay - 4: Uruguay): "))
    se_encontro_patente = False

    for i in range(len(arreglo_registros)):
        if arreglo_registros[i].patente == patente_a_buscar and arreglo_registros[i].pais_cabina == pais_de_cabina:
            print("\nPais del vehiculo:", pais[pais_de_vehiculo(arreglo_registros[i].patente)])
            print("patente:", arreglo_registros[i].patente)
            print("pais de cabina:", pais_cabina(arreglo_registros[i].pais_cabina))
            print("Kilometros:", arreglo_registros[i].kilometros)
            print("forma de pago:", forma_de_pago(arreglo_registros[i].forma_pago))
            print("tipo de vehiculo:", tipo_vehiculo(arreglo_registros[i].tipo_vehiculo))
            print("Codigo identificacion de ticket:", arreglo_registros[i].id)

            se_encontro_patente = True
            break
    if not se_encontro_patente:
        print("\n===============================================")
        print("No existe registro de la patente en el sistema.")
        print("===============================================\n")


def buscar_id(arreglo_registros):
    codigo = str(cargar_identificador(10, mensaje="\nIngrese identificador (debe contener maximo 10 digitos): "))
    codigo_ticket = codigo.zfill(10)
    se_encontro_codigo = False

    for i in range(len(arreglo_registros)):
        if arreglo_registros[i].id == codigo_ticket:
            if arreglo_registros[i].forma_pago == "1":
                arreglo_registros[i].forma_pago = "2"
            elif arreglo_registros[i].forma_pago == "2":
                arreglo_registros[i].forma_pago = "1"
            se_encontro_codigo = True
            break

    if not se_encontro_codigo:
        print("\n=================================================================")
        print("No existe registro del codigo de ticket ingresado en el sistema.")
        print("=================================================================\n")

    else:
        leerarchivo(arreglo_registros)


def cantidad_vehiculos(arreglo_registros):
    pais = ["Argentina", "Brasil", "Chile", "Bolivia", "Paraguay", "Uruguay", "Otro"]
    cont_vehic_por_pais = 7 * [0]
    for i in range(len(arreglo_registros)):
        cont_vehic_por_pais[pais_de_vehiculo(arreglo_registros[i].patente)] += 1

    for i in range(len(cont_vehic_por_pais)):
        print(pais[i], ":", cont_vehic_por_pais[i])


def ticket(tipo, telepeaje, pais_de_cabina):
    tarifa = 0
    if pais_de_cabina == "0":
        tarifa = 300
    if pais_de_cabina == "2":
        tarifa = 400
    if pais_de_cabina == "4":
        tarifa = 300
    if pais_de_cabina == "3":
        tarifa = 300
    if pais_de_cabina == "1":
        tarifa = 200
    # moto
    if tipo == "0":
        tarifa = int(tarifa * 0.5)
        if telepeaje == "2":
            tarifa = int(tarifa * 0.9)
    # auto
    if tipo == "1":
        tarifa = tarifa
        if telepeaje == "2":
            tarifa = int(tarifa * 0.9)
    # camion
    if tipo == "2":
        tarifa = (tarifa * 1.6)
        if telepeaje == "2":
            tarifa = int(tarifa - (tarifa * 0.1))

    return tarifa


def pago_de_tickets(arreglo_registros):
    vehiculo = ["Motocicleta", "Automovil", "Camion"]
    vec_acumulador = 3 * [0]

    for i in arreglo_registros:
        tarifa = ticket(i.tipo_vehiculo, i.forma_pago, i.pais_cabina)
        vec_acumulador[int(i.tipo_vehiculo)] += tarifa

    for i in range(len(vec_acumulador)):
        print(vehiculo[i], ":", vec_acumulador[i])
    return vec_acumulador


def mayor_monto(montos):
    vehiculo = ["Motocicleta", "Automovil", "Camion"]
    suma_montos_totales = 0
    mayor = None
    vehiculo_mayor = 0

    for i in range(len(montos)):
        if mayor is None or montos[i] > mayor:
            mayor = montos[i]
            vehiculo_mayor = vehiculo[i]
        suma_montos_totales += montos[i]
    print(vehiculo_mayor, ":", mayor)
    print("porcentaje de monto mayor sobre el total: ", porcentaje(suma_montos_totales, mayor), "%")


def porcentaje(total, mayor):
    if total != 0:
        porcent = int((mayor * 100) / total)
    else:
        porcent = total
    return porcent


def distancia_promedio(arreglo_registros):
    acumulador = 0
    acumulador_vehiculos = 0

    for i in range(len(arreglo_registros)):
        acumulador += int(arreglo_registros[i].kilometros)

    promedio = round(acumulador / len(arreglo_registros), 2)

    for i in range(len(arreglo_registros)):
        if float(arreglo_registros[i].kilometros) > promedio:
            acumulador_vehiculos += 1
    print("\npromedio del total de km recorridos en el total de vehiculos: ", promedio)
    print("cantidad vehiculos que recorrrieron distancia mayor al promedio: ", acumulador_vehiculos)


def Principal():
    opcion = -1
    arreglo_registros = []
    vec_acumulador = []
    arreglo_cargado = False
    entro_opcion_7 = False
    while opcion != 0:
        mostrar_menu()
        opcion = validacion_entrada(0, 9, "Ingrese una opcion: ")
        if int(opcion) == 1:
            if len(arreglo_registros):
                while True:
                    entrada = int(input("esta seguro que desea eliminar el arreglo? (1 = Aceptar / 2 = Cancelar): "))
                    if entrada == 1 or entrada == 2:
                        if entrada == 1:
                            arreglo_registros.clear()
                            arreglo_cargado = False
                            break
                        if entrada == 2:
                            break
                    else:
                        print("Debes ingresar un valor numérico válido entre(1 y 2).")
            else:
                arreglo_registros = crear_arreglo()
                arreglo_cargado = True

        elif int(opcion) == 2 and arreglo_cargado:
            vector_nuevo_ticket = nuevo_ticket()
            mi_lista = ''.join(vector_nuevo_ticket)
            cargar_ticket(mi_lista, arreglo_registros)

        elif int(opcion) == 3 and arreglo_cargado:
            leerarchivo(arreglo_registros)

        elif int(opcion) == 4 and arreglo_cargado:
            buscar_patente(arreglo_registros)

        elif int(opcion) == 5 and arreglo_cargado:
            buscar_id(arreglo_registros)

        elif int(opcion) == 6 and arreglo_cargado:
            cantidad_vehiculos(arreglo_registros)

        elif int(opcion) == 7 and arreglo_cargado:
            vec_acumulador = pago_de_tickets(arreglo_registros)
            entro_opcion_7 = True

        elif int(opcion) == 8 and entro_opcion_7:
            mayor_monto(vec_acumulador)

        elif int(opcion) == 9 and arreglo_cargado:
            distancia_promedio(arreglo_registros)

        elif arreglo_cargado == False and opcion != 0:
            print("\n=========================================")
            print("ATENCION! Primero debe cargar el arreglo.")
            print("=========================================\n")

        elif entro_opcion_7 == False and opcion != 0:
            print("\n=========================================================================================")
            print("ATENCION! Primero debe determinar el total de pagos realizados por cada tipo de vehiculo.")
            print("===========================================================================================\n")


if __name__ == '__main__':
    Principal()
