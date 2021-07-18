from binary import to_decimal, to_binary


def binary_notation(ip_decimal):
    ip_decimal_list = ip_decimal.split(sep='.')
    ip_binary_list = []
    for decimal in ip_decimal_list:
        ip_binary_list.append(to_binary(int(decimal)))
    return ip_binary_list


def run():
    ip_decimal = input("Indica la direccion IP en decimal: ")
    binary_list = binary_notation(ip_decimal)
    print('.'.join(binary_list))


if __name__ == '__main__':
    run()