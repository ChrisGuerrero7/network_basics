def get_prefix(ip, n_host):
    pass


def run():
    print("FLSM")
    print("Hallamos la mascara de sebred a partir de la direccion de red y el numero de host.\n")
    network = input("Indica la direccion de red: ")
    num_host = int(input("Indica el numero de host: "))
    prefix_length = get_prefix(network, num_host)
    print(prefix_length)


if __name__ == '__main__':
    run()