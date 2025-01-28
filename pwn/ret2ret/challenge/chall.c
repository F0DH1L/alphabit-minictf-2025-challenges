#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

// gcc chall.c -o chall -fno-stack-protector -no-pie -z relro -z now

void gadgets () {
    int poprdi = 0xc35f;
    int poprsi = 0xc35e;
    int poprdx = 0xc35a;
    int poprax = 0xc358;
    int syscall = 0xc3050f;
}

int main () {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);

    char buf[0x10];
    printf("can you run /bin/sh");
    printf("\ngive me your name: ");

    read(0, buf, 0x100);
}