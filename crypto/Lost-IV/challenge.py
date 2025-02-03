import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from secret import FLAG

KEY = b"secretsenhadji31"
BLOCK_SIZE = 16

IV = os.urandom(16)

PLAINTEXT = b"You Want the flag ? You need to find the lost IV first ! "
PLAINTEXT = PLAINTEXT + FLAG

PLAINTEXT = pad(PLAINTEXT, BLOCK_SIZE)

cipher = AES.new(KEY, AES.MODE_CBC, IV)
CIPHERTEXT = cipher.encrypt(PLAINTEXT)

with open("cbc_iv_recovery.txt", "w") as f:
    f.write("Ciphertext: " + CIPHERTEXT.hex() + "\n")
