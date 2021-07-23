from binary import to_decimal, to_binary, is_binary


def binary_complete(address):
    """
    This function provides 4 octect address conversion to full binary.
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
    This function provides conversion of network mask to prefix length.
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
    This function provides conversion of prefix length to network mask.
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
    This function provides class determination of the IP address and network mask
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
    This function provides ip address verification in decimal notation.
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
    This function provides network mask verification.
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
    This function provides conversion of ip address in decimal to binary notation.
    """
    ip_decimal_list = ip_decimal.split(sep='.')
    ip_binary_list = []
    for decimal in ip_decimal_list:
        ip_binary_list.append(to_binary(int(decimal)))
    return ip_binary_list


def is_ip_binary(ip):
    """
    This function provides ip address verification in binary notation.
    """
    try:
        ip_list = ip.split(sep='.')
        binary = ''.join(ip_list)
        count = 0
        for octect in ip_list:
            if is_binary(octect) == True:
                continue
            else:
                count += 1

        if count == 0 and len(ip_list) == 4 and len(binary) == 32:
            return True
        else:
            return False

    except ValueError:
        return False


def dotted_decimal(ip):
    """
    This function provides conversion of ip address in binary to decimal notation.
    """
    ip_list = ip.split(sep='.')
    ip_decimal = []
    for octect in ip_list:
        oct_dec = to_decimal(octect)
        ip_decimal.append(str(oct_dec))

    return ip_decimal


def run():
    """
    This function gives us tools to convert  IP addresses and network mask.
    """

    # INPUT MENUS
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
    MENU_IP = """
    DIRECCION IP
    1. Convertir de IP decimal a Notacion Binaria
    2. Convertir de Notacion Binaria a IP decimal
    Elige una opcion: """

    # WORKLOOP
    while True:
        option = input(MENU_MAIN)

        # IP ADDRESS OPTION
        if option == '1':
            option_ip = input(MENU_IP)

            # Converting the ip address to binary
            if option_ip == '1':
                ip_decimal = input("\nIndica la direccion IP en decimal: ")
                is_ip = is_ip_decimal(ip_decimal)

                # Verification of ip addess
                if is_ip == True:
                    binary_list = binary_notation(ip_decimal)
                    binary_str = '.'.join(binary_list)
                    print('Notacion Binaria: ' + binary_str)
                    ip_class = class_decimal(ip_decimal)
                    print('Clase de direccion ip: ' + ip_class[0])
                    print('Prefix Length: ' + str(ip_class[1]))
                # Wrong ip address
                else:
                    print('La direccion ingresada no es correcta. Intenta nuevamente')

            # Converting the binary notation to decimal
            elif option_ip == '2':
                ip_binary = input("\nIndica la direccion IP en notacion binaria: ")
                is_notation = is_ip_binary(ip_binary)

                # Verification of binary notation
                if is_notation == True:
                    decimal_list = dotted_decimal(ip_binary)
                    decimal_str = '.'.join(decimal_list)
                    print('Direccion IP: ' + decimal_str)
                # Wrong binary notation
                else:
                    print('La direccion ingresada no es correcta. Intenta nuevamente')

            # Wrong option
            else:
                print('\nOpcion Incorrecta. Intenta nuevamente.')

        # MASK OPTION
        elif option == '2':
            option_mask = input(MENU_MASK)

            # Converting the prefix length to netmask
            if option_mask == '1':
                prefix_length = int(input("\nIndica el prefijo de longitud: "))

                # Verification of prefix length
                if prefix_length <= 32:
                    mask_bin = netmask(prefix_length)
                    mask_dec = [str(to_decimal(x)) for x in mask_bin]
                    mask_str = '.'.join(mask_dec)
                    print('Mascara de red: ' + mask_str)
                # Wrong prefix length
                else:
                    print('Es una mascara de red invalida!')

            # Converting the Netmask to prefix length
            elif option_mask == '2':
                net_mask = input("\nIndica la mascara de red: ")
                is_netmask = is_mask(net_mask)

                # Verification of netmask
                if is_netmask == True:
                    prefix = premask(net_mask)
                    print('Prefijo de longitud: ' + str(prefix))
                # Wrong netmask
                else:
                    print('La mascara ingresada no es correcta. Intenta nuevamente.')

            # Wrong option
            else:
                print('\nOpcion Incorrecta. Intenta nuevamente.')

        # Get out of the loop
        elif option == '3':
            print('\nGRACIAS. VUELVE PRONTO!')
            break
        # Wrong option
        else:
            print('\nOpcion Incorrecta. Intenta nuevamente.')


if __name__ == '__main__':
    run()