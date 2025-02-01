#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/ptrace.h>
#include <errno.h>
#include <string.h>

// gcc chall.c -o chall
// strip --strip-all chall

int is_debugged() {
    if (ptrace(PTRACE_TRACEME, 0, NULL, NULL) == -1) {
        return errno == EPERM; // EPERM means we are already being traced
    }
    return 0;   
}

char data[] = {
    6, 5, 3, 62, 7, 14, 19, 62, 21, 9, 4, 62, 22, 8, 15, 15,
    197, 196, 212, 207, 206, 209, 190, 204, 212, 197, 206, 206, 207, 206, 207, 207};

int main () {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);

    printf("welcome can you get the flag!!!\n");


    char input[0x10];

    printf("input: ");
    read(0x0, input, 0x10);


    if (is_debugged()) {
        for (int i = 0; i < 0x10; i++) {
            input[i] = (input[i] ^ 0x21) - 0x40;
        }
        if (memcmp(input, data, 0x10) == 0) {
            puts("Congrats you got it");
            exit(0);
        }
    } else {
        for (int i = 0; i < 0x10; i++) {
            input[i] = (input[i] ^ 0xff) + 0x34;
        }
        if (memcmp(input, data+0x10, 0x10) == 0) {
            puts("Congrats you got it");
            exit(0);
        }
    }
    
}