from pwn import process,remote
import string
#r = remote('host',port)
p = process("../challenge/chall.py")

p.recvuntil(b'> ')
p.sendline(b'1')
enc = p.recvline()
inp = b'A'
chars = string.ascii_letters + string.digits + '{}_?!'
for j in range(len(enc.decode())//2):
    for i in chars:
        p.sendlineafter(b'> ',b'2')
        p.sendlineafter(b'What do you want to encrypt ? ',inp + i.encode())
        res = p.recvline()
        if (res[:len(res)-1] == enc[:len(inp)*2]):
            inp += i.encode()
            break
print(inp)
