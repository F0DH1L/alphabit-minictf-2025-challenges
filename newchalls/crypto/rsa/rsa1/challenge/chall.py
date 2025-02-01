#usr/bin/env python3 

from Crypto.Util.number import long_to_bytes,bytes_to_long,inverse,getPrime

flag = b'somelongtext'

m = bytes_to_long(flag)

p = getPrime(512)
q = getPrime(512)
n = p * q
e = 0x10001
phi = (p-1)*(q-1)
d = inverse(e,phi)
c = pow(m,e,n)
print(f"{n=}\n{e=}\n{c=}")
x = bytes_to_long(input("Give some text to encrypt : ").encode())
print(pow(x,e,n))
x = int(input("Give me now a ciphertext to decrypt : "))
print(pow(x,d,n))