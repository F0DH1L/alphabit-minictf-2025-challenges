#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// gcc chall.c -o chall -no-stack-protector

void setup () {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
}

int main () {
    setup();

    printf("system: %p\n", system);

    char buf[0x10];
    printf("data: ");
    gets(buf);
}
