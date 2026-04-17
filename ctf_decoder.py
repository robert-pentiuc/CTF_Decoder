from base64 import b64decode
def solve_level_1():
    msg = "666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d"
    result = bytes.fromhex(msg).decode()
    return result

def solve_level_2():
    msg = 'ZmxhZ3t3NDF0XzF0c19hbGxfYjE='
    result64 = b64decode(msg).decode()

    numero = 664813035583918006462745898431981286737635929725
    result10 = numero.to_bytes(length=20, byteorder='big').decode()
    return result64, result10

def solve_level_3():
    msg = 'NjY2YzYxNjc3YjZjMzQ3OTMzNzIzNTVmMzA2ZTVmNmMzNDc5MzM3MjM1N2Q='
    msg_dec = b64decode(msg).decode()
    result = bytes.fromhex(msg_dec).decode()
    return result

def solve_level_4():
    msg = 'Wm14aFozdGlOSE16WDNNeGVIUjVYMll3ZFhKZk1XNWpNM0IwTVRCdWZRPT0='
    msg_dec = b64decode(msg).decode()
    msg_dec2 = b64decode(msg_dec).decode()
    return msg_dec2

def solve_level_5():
    msg = "7d72337474346d5f73337479625f35647234776b6334627b67616c66"
    msg_rev = ""
    for i in range(0, len(msg), 2):
        couple = msg[i: i + 2]
        msg_rev = couple + msg_rev
    result = bytes.fromhex(msg_rev).decode()
    return result

def solve_level_6():
    msg ="0066006c00610067007b007a003300720030005f00700034006400640031006e0067005f0033007600330072007900770068003300720033007d"
    clean_msg = ""
    for i in range(0, len(msg), 4):
        clean_msg += msg[i + 2: i + 4]

    result = bytes.fromhex(clean_msg).decode()
    return result

def solve_level_7():
    msg = "4e6a5932597a59784e6a6333596a63304e6a67334d6a4d7a4d7a4d315a6a5a6a4d7a51334f544d7a4e7a49334d7a566d4e6a517a4d7a4d7a4e7a41335a413d3d"
    result_1 = bytes.fromhex(msg)
    result_2 = b64decode(result_1).decode()
    result_3 = bytes.fromhex(result_2).decode()

    return result_3

def solve_level_8():
    msg = "666c6167 | e20xeA== | 5f346e64 | X200dA== | 63685f33 | bmMwZA== | 316e6735 | fQ=="
    final_msg = ""
    parts = msg.split("|")
    for c in range(len(parts)):
        p = parts[c].strip()
        if c % 2 == 0:
            decoded = bytes.fromhex(p).decode()
        else:
            decoded = b64decode(p).decode()

        final_msg += decoded
    return final_msg

def solve_level_9():
    from caesar_breaker import brute_force
    msg = "bXNobntqNDN6NHlfdDMzYXpfaTR6MzY0fQ=="
    result_1 = b64decode(msg).decode()
    list_k_msg = brute_force(result_1)
    for k, testo in list_k_msg:
        if testo.startswith("flag"):
            return testo





def main():
    print(solve_level_1())
    print(solve_level_2())
    print(solve_level_3())
    print(solve_level_4())
    print(solve_level_5())
    print(solve_level_6())
    print(solve_level_7())
    print(solve_level_8())
    print(solve_level_9())


if __name__ == '__main__':
    main()