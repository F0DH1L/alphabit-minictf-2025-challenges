We decompile the binary, when we find the adress of the main function we disassemble it using gdb to find the offset where the sleep is called, then we have two choices : 
1 - set *add = 0x9090909090
2 - change it with the hexedito the value must be 0xe8aeedffff we change it to 0x9090909090
The other method is to patch directly the binary with ghidra or bninja [this video will help you](https://www.youtube.com/watch?v=LyNyf3UM9Yc&t=3s)
