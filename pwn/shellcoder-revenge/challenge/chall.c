#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>

// gcc chall.c -o chall

void setup () {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
}

int main () {
    setup();

    void (*code)(void) = mmap(0x0, 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0x0);


    printf("give me code: ");
    read(0x0, code, 0x5);

    code();



}
