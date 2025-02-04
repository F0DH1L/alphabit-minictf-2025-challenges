#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/sendfile.h>

// gcc chall.c -o chall -no-pie

void setup () {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
}

void win() {
    int fd = open("./flag.txt", 0x0);
    sendfile(0x1, fd, 0x0, 0x100);

    exit(0);
}


int main () {
    setup();

    char buf[0x10];
    printf("data: ");
    read(0x0, buf, 0x10);
    printf(buf);
    printf("data: ");
    read(0x0, buf, 0x100);
}
