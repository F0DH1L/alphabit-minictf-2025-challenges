from sage.all import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib
import binascii
from Crypto.Util.number import long_to_bytes

# brainpoolP256r1
p = 0xa9fb57dba1eea9bc3e660a909d838d726e3bf623d52620282013481d1f6e5377  
a = 0x7d5a0975fc2c3057eef67530417affe7fb8055c126dc5c6ce94a4b44f330b5d9
b = 0x26dc5c6ce94a4b44f330b5d9bbd77cbf958416295cf7e1ce6bccdc18ff8c07b6
E = EllipticCurve(GF(p), [a, b])

# Alice's Public Key
Alice_pub = E(31192678164488171587110288877800946421422813519585731333526884488717844769347, 
              51590321041911735451880918446498466417115564509246336777426402684510375398109)

# Bob's Private Key
Bob_priv = 47369977161193910001790423628713971907998658545195785788358819057351049525640

# Compute the shared secret (ECDH)
Shared_secret = Bob_priv * Alice_pub
Shared_secret_x = int(Shared_secret[0])  # Use the x-coordinate

print(Shared_secret_x)
print(long_to_bytes(Shared_secret_x))
