from pwn import process
def check(possible_flag):
    p = process("../challenge/chall")
    p.sendline(possible_flag.encode())
    i = p.recv()
    print(i)

flag = 'Alphabit{'
m = [301, 728, 546, 315, 756, 497, 315, 658, 301, 322, 770, 315, 623, 532, 315, 742, 756, 315, 763, 315, 728, 343, 322, 770, 301, 294, 728]
for i in m:
    flag += chr(i//7 + 6)
flag += '_'
flag += "0f_Th3_l0w_l3v3l_"
n = [123, 54, 119, 121, 122, 57, 113]
for i in n:
    flag += chr(i-5)
flag += '_'
flag += bytes.fromhex("6d346368316e337d").decode()
check(flag)