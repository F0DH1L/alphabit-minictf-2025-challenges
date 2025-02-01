#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// gcc chall.c -o chall -no-pie -z relro -z now

void win () {
    system("cat flag.txt");
    exit(0);
}

void setup () {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
}

int main () {
    setup();

    printf("the address of the stored rip is: %p\n", __builtin_frame_address(0)+8);
    void* ptr;
    printf("where to read > ");
    scanf("%p", &ptr);
    printf("reading 0x8 bytes into %p\n", ptr);
    printf("what to read > ");
    read(0, ptr, 0x8);

    puts("Good Luck :)");
    exit(0);
}
