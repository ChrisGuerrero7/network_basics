from ip_address import *


def network(ip, mask):
    """
    This function allows us to find the address from the address of a host.
    """
    class_ip = class_decimal(ip)[0]
    pl = class_decimal(ip)[1]
    binary_ip = binary_notation(ip)
    binary_list = []
    count = 0
    if class_ip == 'C':
        binary = binary_ip[3]
        borrowed_bit = int(mask) - pl
        for bit in binary:
            count += 1
            if count <= borrowed_bit:
                binary_list.append(bit)
            else:
                binary_list.append('0')
        binary = ''.join(binary_list)
        binary_ip[3] = binary
        binary_join = '.'.join(binary_ip)
        ip_network_list = dotted_decimal(binary_join)
        ip_network = '.'.join(ip_network_list)
    return ip_network


def run():
    """
    This program allows us to design the fixed size network (FLSM).
    """
    print("SUBNETTING - FLSM")
    address = input("Indica la direccion IP: ")
    prefix_length = input("Indica el prefijo de longitud: ")
    is_address = is_ip_decimal(address)
    if is_address == True and int(prefix_length) <= 32:
        network_add = network(address, prefix_length)
        print(network_add)
    else:
        print("Direccion IP o Mascara de red incorrecta.")


if __name__ == '__main__':
    run()