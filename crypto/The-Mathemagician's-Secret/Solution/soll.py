from Crypto.Util.number import long_to_bytes


mod = 2**64

equations = [
    (17, 4, 25194994872, 3, 23, 40871185060),
    (17, 4, 42005481930, 3, 23, 45332464339),
    (17, 4, 36745152809, 3, 23, 50026341125),
    (17, 4, 39708733006, 3, 23, 44924205391),
    (17, 4, 39971525569, 3, 23, 47987695993),
    (17, 4, 39599077192, 3, 23, 42691308655),
    (17, 4, 39291744519, 3, 23, 50474244351),
    (17, 4, 467789, 3, 23, 82551),
]

flag = ""
for eq in equations:
    a, b, c1, c, d, c2 = eq

    det = (a * d - b * c) % mod
    det_inv = pow(det, -1, mod)

    x = (d * c1 - b * c2) * det_inv % mod
    y = (-c * c1 + a * c2) * det_inv % mod

    flag_part1 = long_to_bytes(x).decode("utf-8")
    flag_part2 = long_to_bytes(y).decode("utf-8")
    flag += flag_part1 + flag_part2

print(f"Flag: {flag}")
