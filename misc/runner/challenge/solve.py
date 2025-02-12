#!/usr/bin/env python3

import os

print("I am code runner 1.0")
code = "+"*ord('s')+ "!"+ "-"*(ord('s')-ord('h')) +"!$" + "+"*(ord('t') - ord('a')) +"!" + '$'
cells = [0] * 0x100
pointer = 0
cmd = ""

print(code)
for i in range(len(code)):
    # print(cmd)
    # print(pointer)
    # print('=======')
    if code[i] == ">":
        pointer = (pointer + 1) % 0x100
        
    elif code[i] == "<":
        pointer = (pointer - 1) % 0x100
    
    elif code[i] == "+":
        cells[pointer] = (cells[pointer] + 1) % 0x100
    
    elif code[i] == "-":
        cells[pointer] = (cells[pointer] - 1) % 0x100
    
    elif code[i] == "!":
        cmd += chr(cells[pointer])
    
    elif code[i] == "$":
        # run the command!!!
        print(cmd.encode())
        os.system(cmd)
        cmd = ""
print("did you get the flag???")
