def to_binary(number):
    """
    Esta funcion se encarga de convertir un numero decimal en binario.
    """
    list_binary = []
    number_convert = number
    for i in range(7,-1,-1):
        power_binary = 2 ** i
        number_convert -= power_binary
        if number_convert >= 0:
            list_binary.append('1')
        else:
            number_convert += power_binary
            list_binary.append('0')
    str_binary = "".join(list_binary)
    return str_binary


def to_decimal(binary):
    """
    Esta funcion se encarga de convertir un octeto binario en numero decimal.
    """
    decimal = 0
    for i in range(7,-1,-1):
        index = 7 - i
        decimal += (int(binary[index]) * (2 ** i))
    return decimal


def is_binary(binary):
    """
    Esta funcion se encarga de determinar si el numero es binario.
    """
    count = 0
    for bit in binary:
        if bit in ['1', '0']:
            continue
        else:
            count += 1

    if count == 0:
        return True
    else:
        return False


def run():
    MENU = """\nCONVERTIDOR BINARIO
1. Convierte un numero decimal a octeto binario
2. Convierte un octeto binario a numero decimal
3. Salir
Elige una opcion: """
    while True:
        option = input(MENU)
        if option == '1':
            print("\nCONVERTIMOS UN NUMERO DECIMAL (<255) A OCTETO BINARIO")
            number = int(input('Indica el numero decimal: '))
            if number <= 255:
                number_binary = to_binary(number)
                print("Numero en binario: " + number_binary)
            else:
                print("El numero debe ser menor a 255")
        elif option == '2':
            print("\nCONVERTIMOS UN OCTETO BINARIO A DECIMAL")
            binary = input('Indica el octeto binario: ')
            is_octec_binary = is_binary(binary)
            if len(binary) == 8 and is_octec_binary == True:
                number_decimal = to_decimal(binary)
                print("Numero en decimal: " + str(number_decimal))
            else:
                print("El numero debe ser un octeto binario.\nEjemplo: 10101000")
        elif option == '3':
            print("\nGRACIAS, HASTA PRONTO!")
            break
        else:
            print("\nELIGE UNA OPCION DEL MENU!")

if __name__=='__main__':
    run()
