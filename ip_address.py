from binary import to_decimal, to_binary


def is_ip_decimal(ip):
    """
    Esta funcion se encarga de verificar si la direccion ip ingresada es correcta.
    """
    try:
        ip_list = ip.split(sep='.')
        count = 0
        for num in ip_list:
            if int(num) <= 255:
                continue
            else:
                count += 1
        
        if len(ip_list) == 4 and count == 0:
            return True
        else:
            return False
    except ValueError:
        return False


def binary_notation(ip_decimal):
    """
    Esta funcion se encarga de convertir la direccion ip decimal en notacion binaria.
    """
    ip_decimal_list = ip_decimal.split(sep='.')
    ip_binary_list = []
    for decimal in ip_decimal_list:
        ip_binary_list.append(to_binary(int(decimal)))
    return ip_binary_list


def run():
    MENU_MAIN = """
    DIRECCION IP Y MASCARA DE RED
    1. Direccion IP
    2. Mascara de red
    3. Salir
    Elige una opcion: """
    while True:
        option = input(MENU_MAIN)
        if option == '1':
            ip_decimal = input("\nIndica la direccion IP en decimal: ")
            is_ip = is_ip_decimal(ip_decimal)
            if is_ip == True:
                binary_list = binary_notation(ip_decimal)
                binary_str = '.'.join(binary_list)
                print('Notacion Binaria: ' + binary_str)
            else:
                print('La direccion ingresada no es correcta. Intenta nuevamente')
        elif option == '2':
            #mask_decimal = input("\nIndica la mascara de red en decimal: ")
            #is_mask = is_mask_decimal(mask_decimal)
            #if is_mask == True:
            #    mask_binary = netmask(mask_decimal)
            #    mask_binary_str = '.'.join(mask_binary)
            #    print('Mascara de red en binario: ' + mask_binary_str)
            pass
        elif option == '3':
            print('\nGRACIAS. VUELVE PRONTO!')
            break
        else:
            print('\nOpcion Incorrecta. Intenta nuevamente.')


if __name__ == '__main__':
    run()