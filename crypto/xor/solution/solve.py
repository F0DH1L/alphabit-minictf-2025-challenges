from pwn import xor
import string

flag_chars = string.ascii_letters + string.digits + '{_}'

def is_printable(byte_data):
    return all(chr(byte) in flag_chars for byte in byte_data)

ct = "380eadd0410347f1430277261bedcd7f0a40b54f14743752a8ff483e7acd0b054e205288e74b2f1ef2677a652656b1d44c0d42e954276c"


first_part = xor(bytes.fromhex(ct[:18]),b"Alphabit{")
second_part = xor(bytes.fromhex("6c"),b"}")
possible_keys= [first_part + chr(i).encode() + second_part for i in range(256)]
for key in possible_keys :
    flag = xor(bytes.fromhex(ct),key)
    if is_printable(flag):
        print(flag)
