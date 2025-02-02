#usr/bin/env python3
from Crypto.Util.number import long_to_bytes,bytes_to_long,getPrime

flag = b"Alphabit{How_D1d_y0u_solV3_1t_wi70uT_th3_modulo?}"
p = getPrime(512)
q = getPrime(512)
n = p*q
e = 0x10001
m = bytes_to_long(flag)
c = pow(m,e,n)
print(f"{c=}\n{e=}")
x = bytes_to_long(input("Give some text to encrypt : ").encode())
print(pow(x,e,n))
x = int(input("Give me now a ciphertext to decrypt : "))
print(pow(x,d,n))