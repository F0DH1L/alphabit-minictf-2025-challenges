#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>


// gcc chall.c -o chall -no-pie

int main () {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);

    int fd = open("/proc/self/mem", 0x1);

    void* addr;
    char byte;


    printf("address to patch: ");
    scanf("%p", &addr);

    printf("value to put: ");
    read(0x0, &byte, 0x1);

    pwrite(fd, &byte, 0x1, addr);

    printf("program starts now:\n");

    int fd2 = open("/dev/urandom", 0x0);
    unsigned long value, guess;
    read(fd2, &value, 0x8);


    printf("guess the random value: ");
    scanf("%ld", &guess);
    if (guess != value) {
        printf("gg");
        exit(1);
    } else {
        system("cat flag.txt");
    }

}
