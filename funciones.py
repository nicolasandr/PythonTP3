class Ticket:
    def __init__(self, id, patent, tipo_de_vehiculo, forma_de_pago, pais_cabina, kilomentros):
        self.id = id
        self.patente = patent
        self.tipo_vehiculo = tipo_de_vehiculo
        self.forma_pago = forma_de_pago
        self.pais_cabina = pais_cabina
        self.kilometros = kilomentros

    def __str__(self):
        r = str(self.id) + "\t" + str(self.patente) + "\t" + str(self.tipo_vehiculo) + "\t" + str(
            self.forma_pago) + "\t" + str(self.pais_cabina) + "\t" + str(self.kilometros)
        return r


def codigo_patente(valor, tamanio, mensaje):
    caracteres_sin_espacio = 0

    while not valor == tamanio:
        print("Error, debe ingresar un valor que contenga", valor, "digitos 0 6 digitos si la patente es chilena!")
        print(valor, "y", tamanio)
        caracteres_sin_espacio = str(input(mensaje).replace(" ", ""))
        tamanio = len(caracteres_sin_espacio)

    return caracteres_sin_espacio


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
                print("Error, debe ingresar un numero que contenga hasta", valor, "caracteres numericos!.")
        else:
            print("Debes ingresar un valor numérico válido entre(0-9999999999) .")

    return val


def tipo_vehiculo_o_pais_cabina(valor1, valor2, mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            valor = int(entrada)

            if valor1 <= valor <= valor2:
                break
            else:
                print("Error, debe ingresar un numero entre", valor1, "y", valor2, "!.")
        else:
            print("Debes ingresar un valor numérico válido.")
    return valor


def forma_pago(manual, telepeaje, mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            valor = int(entrada)

            if valor == manual or valor == telepeaje:
                break
            else:
                print("Error, debe ingresar un numero entre", manual, "y", telepeaje, ". (1: manual, 2 telepeaje)!")
        else:
            print("Debes ingresar un valor numérico válido.")

    return valor


def patente(mensaje):
    while True:
        entrada = input(mensaje).replace(" ", "")

        if len(entrada) == 6:
            entrada = " " + entrada  # Agrega un espacio al principio si la longitud es 6
            break
        elif len(entrada) == 7:
            break
        else:
            print("La patente debe tener 6 o 7 dígitos. Inténtalo nuevamente.")

    return entrada


def pais_de_vehiculo(patente):

    if len(patente) == 7:
        if patente[0:2].isalpha() and patente[2:5].isdigit() and patente[5:7].isalpha():
            # argentina AA333AA
            procedencia_vehiculo = "Argentina"

        elif patente[0:3].isalpha() and patente[3].isdigit() and patente[4].isalpha() and patente[5:7].isdigit():
            # brasil
            procedencia_vehiculo = "Brasil"
        elif patente[0] == " " and patente[1:5].isalpha() and patente[5:7].isdigit():
            # chile
            procedencia_vehiculo = "Chile"
        elif patente[0:2].isalpha() and patente[2:].isdigit():
            # Bolivia
            procedencia_vehiculo = "Bolivia"
        elif patente[0:4].isalpha() and patente[4:].isdigit():
            # paraguay
            procedencia_vehiculo = "Paraguay"
        elif patente[0:3].isalpha() and patente[3:].isdigit():
            # uruguay
            procedencia_vehiculo = "Uruguay"
        else:
            # otro
            procedencia_vehiculo = "Otro"
    else:
        procedencia_vehiculo = "Otro"

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
    vector_ticket.append(str(tipo_vehiculo_o_pais_cabina(0, 2, mensaje="\nIngrese el tipo de vehiculo: (0: motocicleta,"
                                                                       "1: automóvil, ""2: camión): ")))
    # forma de pago
    vector_ticket.append(str(forma_pago(1, 2, mensaje="\ningrese la forma de pago (1: manual, 2 telepeaje): ")))
    # pais cabina
    vector_ticket.append(str(tipo_vehiculo_o_pais_cabina(0, 4, mensaje="\nIngrese donde se encuentra la cabina (0: "
                                                                       "Argentina - 1: Bolivia - 2: Brasil - 3: "
                                                                       "Paraguay - 4: Uruguay): ")))
    # distancia en km
    distancia = str(tipo_vehiculo_o_pais_cabina(0, 999, mensaje="\nIngrese la distancia en Km entre (0 y 999): "))
    vector_ticket.append(distancia.zfill(3))

    return vector_ticket
