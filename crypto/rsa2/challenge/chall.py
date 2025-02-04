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
x = int(input("Give me a number to encrypt : "))
print(pow(x,e,n))
x = int(input("Give me now a ciphertext to decrypt : "))
if x!=c or x%c!=0:
  print(pow(x,d,n))
else :
  print("Noo!")
