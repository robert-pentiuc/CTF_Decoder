from base64 import b64decode

from caesar_breaker import brute_force


def solve_level_1():
    msg = "666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d"
    msg_bytes = bytes.fromhex(msg).decode()
    return msg_bytes

def solve_level_2():
    msg = 'ZmxhZ3t3NDF0XzF0c19hbGxfYjE='
    msg_dec64 = b64decode(msg).decode()

    num = 664813035583918006462745898431981286737635929725
    num_to_bytes= num.to_bytes(length=20, byteorder='big').decode()
    return msg_dec64, num_to_bytes

def solve_level_3():
    msg = 'NjY2YzYxNjc3YjZjMzQ3OTMzNzIzNTVmMzA2ZTVmNmMzNDc5MzM3MjM1N2Q='
    msg_dec64 = b64decode(msg).decode()
    msg_bytes = bytes.fromhex(msg_dec64).decode()
    return msg_bytes

def solve_level_4():
    msg = 'Wm14aFozdGlOSE16WDNNeGVIUjVYMll3ZFhKZk1XNWpNM0IwTVRCdWZRPT0='
    msg_dec64 = b64decode(msg).decode()
    msg_dec64_2 = b64decode(msg_dec64).decode()
    return msg_dec64_2

def solve_level_5():
    msg = "7d72337474346d5f73337479625f35647234776b6334627b67616c66"
    msg_reversed = ""
    for i in range(0, len(msg), 2):
        couple = msg[i: i + 2]
        msg_reversed = couple + msg_reversed
    msg_bytes = bytes.fromhex(msg_reversed).decode()
    return msg_bytes

def solve_level_6():
    msg ="0066006c00610067007b007a003300720030005f00700034006400640031006e0067005f0033007600330072007900770068003300720033007d"
    clean_msg = ""
    for i in range(0, len(msg), 4):
        clean_msg += msg[i + 2: i + 4]

    msg_bytes = bytes.fromhex(clean_msg).decode()
    return msg_bytes

def solve_level_7():
    msg = "4e6a5932597a59784e6a6333596a63304e6a67334d6a4d7a4d7a4d315a6a5a6a4d7a51334f544d7a4e7a49334d7a566d4e6a517a4d7a4d7a4e7a41335a413d3d"
    msg_bytes = bytes.fromhex(msg)
    msg_dec64 = b64decode(msg_bytes).decode()
    msg_bytes_2 = bytes.fromhex(msg_dec64).decode()

    return msg_bytes_2

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


def solve_level_10():
    from base64 import b64decode

    msg = "pHSjnRW0lF9iW2AgIjXuHjXynP8jmtBpnDL5o2nrlQI="
    msg_search = brute_force(msg)

    for k, testo in msg_search:
        try:
            decoded_bytes = b64decode(testo)
            decoded_text = decoded_bytes.decode(errors="ignore")
        except Exception:
            continue

        if "flag{" in decoded_text:
            return decoded_text

    return "Flag non trovata"


def main():
    print("Livello 1 : ", solve_level_1())
    print("Livello 2 : ", solve_level_2())
    print("Livello 3 : ", solve_level_3())
    print("Livello 4 : ", solve_level_4())
    print("Livello 5 : ", solve_level_5())
    print("Livello 6 : ", solve_level_6())
    print("Livello 7 : ", solve_level_7())
    print("Livello 8 : ", solve_level_8())
    print("Livello 9 : ", solve_level_9())
    print("Livello 10 : ", solve_level_10())


if __name__ == '__main__':
    main()