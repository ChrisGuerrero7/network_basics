from ip_address import class_decimal, netmask
from subnetting import *


def get_prefix(ip, n_host):
    """
    This function allows us to find the netmask from the network address and the hosts number.
    """
    pl = 32 - class_decimal(ip)[1]
    potential_list_host = {}

    for i in range(pl+1):
        class_host = (2 ** i) - 2
        if class_host >= n_host:
            potential_list_host[class_host] = i

    potential_host = min(potential_list_host.keys())
    bit_host = potential_list_host[potential_host]
    prefix = 32 - bit_host
    return prefix


def run():
    print("FLSM - Netmask")
    network = input("Indica la direccion de red: ")
    num_host = int(input("Indica el numero de host: "))
    prefix_length = get_prefix(network, num_host)
    mask_list = netmask(prefix_length)
    mask = '.'.join(mask_list)
    broadcast = get_address(network, str(prefix_length), 1)
    first_address = '.'.join(get_limits(network, "first"))
    last_address = '.'.join(get_limits(broadcast, "last"))
    print("Prefijo de longitud: " + str(prefix_length))
    print("Netmask: " + mask)
    print("Broadcast: " + broadcast)
    print("Rango de IPs: " + first_address + " - " + last_address)


if __name__ == '__main__':
    run()