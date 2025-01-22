from pwn import process

p = process("../challenge/chall")
p.sendline(b"2")
p.send("ALPHABIT")
print(p.recvline())