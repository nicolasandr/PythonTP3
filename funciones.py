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
