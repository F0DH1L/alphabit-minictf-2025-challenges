from pwn import xor
import os

flag = "Alphabit{fakeflag}"

key = os.urandom(11)

ct = xor(flag.encode(),key)
print(ct.hex())
print(key)