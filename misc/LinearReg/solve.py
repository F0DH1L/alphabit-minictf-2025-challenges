from pwn import *

io = remote('challenges.alphabit.club', 1337)

# io.sendline('12 34 54 65 67 89 34 12 45 67 45 22 34 56 78 45 23 76 85 23 86 24 19 23 54')

b = 77



for i in range(25):
    io.sendline('0 ' * i + '1 ' + '0 ' * (24 - i))
    io.recvuntil(b'Prediction: ')
    pred = int(io.recvline().replace(b' $', b'').strip())
    print(chr(pred-b), end='')

# io.interactive()