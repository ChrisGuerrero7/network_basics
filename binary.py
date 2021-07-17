def to_binary(number):
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


def run():
    print("CONVERTIMOS UN NUMERO DECIMAL (<255) A OCTETO BINARIO")
    number = int(input('Indica el numero decimal: '))
    if number <= 255:
        number_binary = to_binary(number)
        print("Numero en binario: " + number_binary)
    else:
        print("El numero debe ser menor a 255")    


if __name__=='__main__':
    run()