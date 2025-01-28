from secret import FLAG
from random import randint

def prepare(sugar,salt):
    pate = ""
    weight = len(salt)
    for i,char in enumerate(sugar[::-1]):
        bit_of_salt = salt[i % weight]
        some_pate = chr(ord(char)^ord(bit_of_salt))
        pate += some_pate
    return pate

def bake(pate,oil):
    cake = []
    for some_pate in pate:
        cake.append(ord(some_pate)*oil)
    return cake


a = randint(1,10)
b = randint(1,10)
c = randint(1,10)
p = pow(a,b,c)
q = pow(c,b,a)
oil= p-q
pate = prepare(FLAG.decode(),"salt")
cake = bake(pate,oil)
print(cake)
result_cake = [14, 15, 3, 28, 7, 24, 28, 43, 27, 21, 93, 3, 44, 18, 25, 27, 66, 2, 93, 24, 64, 5, 51, 7, 66, 62, 9, 7, 1, 82, 26, 71, 1, 26, 24, 29, 17, 0, 4, 4, 31, 32]
