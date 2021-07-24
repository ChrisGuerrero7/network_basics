def network(address, mask):
    """
    This function allows us to find the network address from the address of a host.
    """


def run():
    """
    This program allows us to design the fixed size network (FLSM)
    """
    print("SUBNETTING - FLSM")
    address = input("Indica la direccion IP: ")
    prefix_length = input("Indica la mascara de red: ")
    network_add = network(address, prefix_length)
    print(network_add)


if __name__ == '__main__':
    run()