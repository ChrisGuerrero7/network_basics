from binary import to_decimal, to_binary


def binary_complete(address):
    """
    Esta funcion se encarga de convertir una direccion de 4 octetos en binario completo.
    """
    address_list = address.split(sep='.')
    address_binary = []

    for octect in address_list:
        oct_bin = to_binary(int(octect))
        address_binary.append(oct_bin)
    binary = ''.join(address_binary)
    return binary


def premask(mask):
    """
    Esta funcion se encarga de convertir la mascara de red en un prefijo de longitud.
    """
    binary = binary_complete(mask)
    count = 0
    
    for bit in binary:
        if bit == '1':
            count += 1
        elif bit == '0':
            continue

    return count


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
def class_decimal(ip):
    """
    Esta funcion se encarga de determinar a que clase pertenece la direccion ip ingresada y cual es su mascara de red.
    """
    classes = {'A': 8, 'B': 16, 'C': 24, 'D': 0, 'E': 0}
    ip_list = ip.split(sep='.')
    first_octect = int(ip_list[0])
    class_ip = ''
    if first_octect >= 0 and first_octect < 128:
        class_ip = 'A'
    elif first_octect >= 128 and first_octect < 192:
        class_ip = 'B'
    elif first_octect >= 192 and first_octect < 224:
        class_ip = 'C'
    elif first_octect >= 224 and first_octect < 240:
        class_ip = 'D'
    elif first_octect >= 240 and first_octect < 256:
        class_ip = 'E'

    return class_ip, classes[class_ip]


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

def is_mask(mask):
    """
    Esta funcion se encarga de verificar si la mascara de red ingresada es correcta.
    """
    is_decimal = is_ip_decimal(mask)
    binary_mask = binary_complete(mask)
    count = 0

    for i in range(len(binary_mask)):
        if i == (len(binary_mask) - 1):
            break
        
        if (binary_mask[i] == '0') and (binary_mask[i + 1] == '1'):
            count += 1
        else:
            continue

    if is_decimal == True and count == 0:
        return True
    else:
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
    MENU_MASK = """
    MASCARA DE RED
    1. Convertir de prefijo de longitud a netmask
    2. Convertir de netmask a prefijo de longitud
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
                ip_class = class_decimal(ip_decimal)
                print('Clase de direccion ip: ' + ip_class[0])
                print('Prefix Length: ' + str(ip_class[1]))
            else:
                print('La direccion ingresada no es correcta. Intenta nuevamente')
        elif option == '2':
            option_mask = input(MENU_MASK)
            if option_mask == '1':
                prefix_length = int(input("\nIndica el prefijo de longitud: "))
                if prefix_length <= 32:
                    mask_bin = netmask(prefix_length)
                    mask_dec = [str(to_decimal(x)) for x in mask_bin]
                    mask_str = '.'.join(mask_dec)
                    print('Mascara de red: ' + mask_str)
                else:
                    print('Es una mascara de red invalida!')
            elif option_mask == '2':
                net_mask = input("\nIndica la mascara de red: ")
                is_netmask = is_mask(net_mask)
                if is_netmask == True:
                    prefix = premask(net_mask)
                    print('Prefijo de longitud: ' + str(prefix))
                else:
                    print('La mascara ingresada no es correcta. Intenta nuevamente.')
            else:
                print('\nOpcion Incorrecta. Intenta nuevamente.')
        elif option == '3':
            print('\nGRACIAS. VUELVE PRONTO!')
            break
        else:
            print('\nOpcion Incorrecta. Intenta nuevamente.')


if __name__ == '__main__':
    run()