class Ticket:
    def __init__(self, id, patent, tipo_de_vehiculo, forma_de_pago, pais_cabina, kilomentros):
        self.id = id
        self.patente = patent
        self.tipo_vehiculo = tipo_de_vehiculo
        self.forma_pago = forma_de_pago
        self.pais_cabina = pais_cabina
        self.kilometros = kilomentros

    def __str__(self):
        r = "Nro_Ticket:" + str(self.id) + "\t" + "Patente:" + str(self.patente) + "\t\t" + "Vehiculo:" + str(
            self.tipo_vehiculo) + "\t\t" + "Forma_pago:" + str(
            self.forma_pago) + "\t" + "Pais_cabina:" + str(self.pais_cabina) + "\t" + "Km:" + str(self.kilometros)
        return r


def cant_caracteres(valor, num):
    tamanio = len(num)
    if tamanio == valor:
        return True
    else:
        return False


def es_digito(car):
    caracter = str(car)
    if caracter in "0123456789":
        return True
    return False


def porcentaje(total, mayor):
    if total != 0:
        porcent = int((mayor * 100) / total)
    else:
        porcent = total
    return porcent


def forma_de_pago(pago):
    forma_pag = 0

    if pago == "1":
        forma_pag = "manual"
    if pago == "2":
        forma_pag = "Telepeaje"

    return forma_pag


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


def tipo_vehiculo(vehiculo):
    tipo = 0
    if vehiculo == "0":
        tipo = "Motocicleta"
    if vehiculo == "1":
        tipo = "Automovil"
    if vehiculo == "2":
        tipo = "Camion"

    return tipo


def cargar_identificador(valor, mensaje="Ingrese un valor: "):
    while True:
        entrada = input(mensaje).replace(" ", "")
        if entrada.isdigit():
            val = str(entrada)
            tamanio = len(val)

            if 0 < tamanio <= valor:
                break
            else:
                print("\n==========================================================================")
                print("Error, debe ingresar un numero que contenga hasta", valor, "caracteres numéricos!.")
                print("==========================================================================\n")
        else:
            print("\n===========================================================")
            print("ATENCION! Debes ingresar un valor numérico válido entre(0-9999999999) .")
            print("=============================================================\n")

    return val


def validacion_entrada(valor1, valor2, mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            valor = int(entrada)

            if valor1 <= valor <= valor2:
                break
            else:
                print("\n=============================================")
                print("Error, debe ingresar un numero entre", valor1, "y", valor2, "!.")
                print("=============================================\n")
        else:
            print("\n========================================")
            print("Debes ingresar un valor numérico válido.")
            print("========================================\n")
    return valor


def forma_pago(manual, telepeaje, mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            valor = int(entrada)

            if valor == manual or valor == telepeaje:
                break
            else:
                print("\n==========================================================================================")
                print("Error, debe ingresar un numero entre", manual, "y", telepeaje, ". (1: manual, 2 telepeaje)!")
                print("==========================================================================================\n")
        else:
            print("\n========================================")
            print("Debes ingresar un valor numérico válido.")
            print("========================================\n")

    return valor


def patente(mensaje):
    while True:
        entrada = input(mensaje).replace(" ", "")
        entrada_mayusculas = entrada.upper()
        if len(entrada_mayusculas) == 6:
            entrada_mayusculas = " " + entrada_mayusculas  # Agrega un espacio al principio si la longitud es 6
            break
        elif len(entrada_mayusculas) == 7:
            break
        else:
            print("\n===========================================================")
            print("La patente debe tener 6 o 7 dígitos. Inténtalo nuevamente.")
            print("=============================================================\n")
    return entrada_mayusculas


def pais_de_vehiculo(patentee):
    if len(patentee) == 7:
        if patentee[0:2].isalpha() and patentee[2:5].isdigit() and patentee[5:7].isalpha():
            # argentina AA333AA
            procedencia_vehiculo = 0

        elif patentee[0:3].isalpha() and patentee[3].isdigit() and patentee[4].isalpha() and patentee[5:7].isdigit():
            # brasil
            procedencia_vehiculo = 1
        elif patentee[0] == " " and patentee[1:5].isalpha() and patentee[5:7].isdigit():
            # chile
            procedencia_vehiculo = 2
        elif patentee[0:2].isalpha() and patentee[2:].isdigit():
            # Bolivia
            procedencia_vehiculo = 3
        elif patentee[0:4].isalpha() and patentee[4:].isdigit():
            # paraguay
            procedencia_vehiculo = 4
        elif patentee[0:3].isalpha() and patentee[3:].isdigit():
            # uruguay
            procedencia_vehiculo = 5
        else:
            # otro
            procedencia_vehiculo = 6
    else:
        # Otro
        procedencia_vehiculo = 6

    return procedencia_vehiculo


def nuevo_ticket():
    # id
    vector_ticket = []
    id = str(cargar_identificador(10, mensaje="\nIngrese identificador (debe contener maximo 10 digitos): "))
    vector_ticket.append(id.zfill(10))
    # patente
    vector_ticket.append(patente(mensaje="\nIngrese patente (debe contener 7 digitos o 6 digitos si la patente es "
                                         "chilena): "))
    # tipo de vehiculo
    vector_ticket.append(str(validacion_entrada(0, 2, mensaje="\nIngrese el tipo de vehiculo: (0: motocicleta,"
                                                              "1: automóvil, ""2: camión): ")))
    # forma de pago
    vector_ticket.append(str(forma_pago(1, 2, mensaje="\ningrese la forma de pago (1: manual, 2 telepeaje): ")))
    # pais cabina
    vector_ticket.append(str(validacion_entrada(0, 4, mensaje="\nIngrese donde se encuentra la cabina (0: "
                                                              "Argentina - 1: Bolivia - 2: Brasil - 3: "
                                                              "Paraguay - 4: Uruguay): ")))
    # distancia en km
    distancia = str(validacion_entrada(0, 999, mensaje="\nIngrese la distancia en Km entre (0 y 999): "))
    vector_ticket.append(distancia.zfill(3))

    return vector_ticket
