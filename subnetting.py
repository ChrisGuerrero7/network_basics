from ip_address import *


def add_bits(binary, borrow_bit, netbit):
    """
    This function allows us to add zeros to the octect depending on the borrowed bits.
    """
    binary_list = []
    count = 0
    for bit in binary:
        count += 1
        if count <= borrow_bit:
            binary_list.append(bit)
        else:
            binary_list.append(netbit)
    return binary_list


def get_address(ip, mask, netbit):
    """
    This function allows us to find the address from the address of a host.
    """
    dict_class = {'C': 3, 'B': 2, 'A': 1}
    class_ip = class_decimal(ip)[0]
    pl = class_decimal(ip)[1]
    binary_ip = binary_notation(ip)
    x = dict_class[class_ip]
    borrowed_bit = int(mask) - pl
    count_1 = 0
    count_2 = 0
    octect_list = []
    use_octect_list = []

    for oct in binary_ip:
        count_1 += 1
        if count_1 > x:
            use_octect_list.append(oct)
    use_octect = ''.join(use_octect_list)
    binary_list = add_bits(use_octect, borrowed_bit, str(netbit))
    
    for bit in binary_list:
        count_2 += 1
        octect_list.append(bit)
        if count_2 == 8:
            octect = ''.join(octect_list)
            binary_ip[x] = octect
            octect_list = []
            count_2 = 0
            x += 1
    
    ip = '.'.join(dotted_decimal('.'.join(binary_ip)))
    return ip


def get_limits(address, add_type):
    """
    This function allows us to find the network address range
    """
    list_address = address.split('.')
    last_octect = int(list_address[3])
    if add_type == "first":
        last_octect += 1
    elif add_type == "last":
        last_octect -= 1

    list_address[3] = str(last_octect)
    return list_address


def get_hosts(mask):
    """
    This function allows us to find the hosts number
    """
    n_bits = 32 - int(mask)
    n_hosts = (2 ** n_bits) - 2
    return n_hosts

    

def run():
    """
    This program allows us to design the fixed size network (FLSM).
    """
    print("SUBNETTING - FLSM")
    address = input("Indica la direccion IP: ")
    prefix_length = input("Indica el prefijo de longitud: ")
    is_address = is_ip_decimal(address)
    if is_address == True and int(prefix_length) <= 32:
        network = get_address(address, prefix_length, 0)
        broadcast = get_address(address, prefix_length, 1)
        first_address = '.'.join(get_limits(network, "first"))
        last_address = '.'.join(get_limits(broadcast, "last"))
        n_hosts = get_hosts(prefix_length)
        print("- Direccion de Red: " + network)
        print("- Primera direccion usable: "+ first_address)
        print("- Ultima direccion usable: "+ last_address)
        print("- Direccion de Broadcast: " + broadcast)
        print("- Numero de hosts: " + str(n_hosts))
    else:
        print("Direccion IP o Mascara de red incorrecta.")


if __name__ == '__main__':
    run()