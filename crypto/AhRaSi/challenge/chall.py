from secret import FLAG
from Crypto.Util.number import bytes_to_long,getPrime

m = bytes_to_long(FLAG)

p=getPrime(1024)
q=getPrime(1024)
n=p*q
e = 0x10001
e1 = getPrime(256)
e2 = getPrime(256)
c1 = pow((2*p+3*q),e1,n)
c2 = pow((5*p+7*q),e2,n)
c = pow(m,e,n)
with open("output.txt", "w") as f:
    f.write(f"{n=}\n{e=}\n{c=}\n{e1=}\n{e2=}\n{c1=}\n{c2=}")
