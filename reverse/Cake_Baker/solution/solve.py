from pwn import xor
cipher = [14, 15, 3, 28, 7, 24, 28, 43, 27, 21, 93, 3, 44, 18, 25, 27, 66, 2, 93, 24, 64, 5, 51, 7, 66, 62, 9, 7, 1, 82, 26, 71, 1, 26, 24, 29, 17, 0, 4, 4, 31, 32]

for i in range(-19,19):
    if i == 0:
        continue
    else :
        try:
            semi_decrypted = "".join([chr(j//i) for j in cipher]).encode()
            possible_flag = xor(semi_decrypted,b"salt")
            if b'Alpha' in possible_flag[::-1]:
                print(possible_flag[::-1].decode())
        except:
            pass
