def solve_level_1():
    msg = "666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d"
    result = bytes.fromhex(msg)
    return result

def solve_level_2():
    from base64 import b64decode
    msg = 'ZmxhZ3t3NDF0XzF0c19hbGxfYjE='
    result64 = b64decode(msg)

    numero = 664813035583918006462745898431981286737635929725
    result10 = numero.to_bytes(length=20, byteorder='big')
    return result64, result10

def solve_level_3():
    from base64 import b64decode
    msg = 'NjY2YzYxNjc3YjZjMzQ3OTMzNzIzNTVmMzA2ZTVmNmMzNDc5MzM3MjM1N2Q='
    msg_dec = b64decode(msg)
    result = bytes.fromhex(msg_dec)
    return result




def main():
    print(solve_level_1())
    print(solve_level_2())
    print(solve_level_3())


if __name__ == '__main__':
    main()