from ip_address import is_ip_decimal


def run():
    """
    This program allows us to design the fixed size network (FLSM).
    """
    print("SUBNETTING - FLSM")
    address = input("Indica la direccion IP: ")
    prefix_length = input("Indica el prefijo de longitud: ")
    is_address = is_ip_decimal(address)
    if is_address == True and int(prefix_length) <= 32:
        pass


if __name__ == '__main__':
    run()