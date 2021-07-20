from binary import to_decimal, to_binary


def netmask(prefix):
    """
    Esta funcion se encarga de convertir el prefijo de longitud en mascara de red.
    """
    num_prefix = prefix
    mask_list = []
    octect_mask = ''
    for i in range(4):
        if num_prefix % 8 == 0:
            if num_prefix == 0:
                octect_mask = '0' * 8
                num_prefix = 0
            else:
                octect_mask = '1' * 8
                num_prefix = num_prefix - 8
        else:
            if num_prefix > 8:
                octect_mask = '1' * 8
                num_prefix = num_prefix - 8
            elif num_prefix < 8:
                bit_up = num_prefix
                bit_down = 8 - bit_up
                octect_mask = '1' * (bit_up) + '0' * (bit_down)
                num_prefix = 0
        mask_list.append(octect_mask)
        octect_mask = ''
    return mask_list


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
            prefix_length = int(input("\nIndica el prefijo de longitud: "))
            if prefix_length <= 32:
                mask_bin = netmask(prefix_length)
                mask_dec = [str(to_decimal(x)) for x in mask_bin]
                mask_str = '.'.join(mask_dec)
                print('Mascara de red: ' + mask_str)
            else:
                print('Es una mascara de red invalida!')
        elif option == '3':
            print('\nGRACIAS. VUELVE PRONTO!')
            break
        else:
            print('\nOpcion Incorrecta. Intenta nuevamente.')


if __name__ == '__main__':
    run()