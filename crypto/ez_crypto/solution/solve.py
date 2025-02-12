from pwn import process,remote
import string
#r = remote('0.0.0.0',1337)
p = process("../challenge/chall.py")

p.recvuntil(b'> ')
p.sendline(b'1')
enc = p.recvline()
inp = b'Alphabit{'
chars = string.ascii_letters + string.digits + '{}_?!'
for j in range(len(enc.decode())//2):
    for i in chars:
        p.sendlineafter(b'> ',b'2')
        p.sendlineafter(b'What do you want to encrypt ? ',inp + i.encode())
        res = p.recvline()
        if (enc.decoce().startswith(res.decode()):
            inp += i.encode()
            break

open("flag.txt","w").write(inp.decode())
