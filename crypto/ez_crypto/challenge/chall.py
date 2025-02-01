#!/usr/bin/env python3
from secret import FLAG,encrypt

print("You have two options:")
print("1 - Print the encypted flag")
print("2 - Encrypt your input")

while True:
    x = input("> ")
    if x == "1":
        print(encrypt(FLAG))
        print()
    elif x == "2":
        print()
        pt = input("What do you want to encrypt ? ")
        print(encrypt(pt))
        print()
    else :
        break
