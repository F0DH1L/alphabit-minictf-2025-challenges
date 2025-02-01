#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

// gcc chall.c -o chall

void setup () {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
}

unsigned long* addrs[4];

int main () {
    setup();

    int fd = open("/dev/urandom", 0x0);

    for (int i = 0; i < 4; i++) {
        addrs[i] = (unsigned long *)mmap(0x0, 0x1000, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0x0);
        read(fd, addrs[i], 0x8);
        printf("addr %d: %p\n", i, addrs[i]);
    }

    char buf[0x1000];
    read(0x0, buf, 0x1000);
    printf(buf);

    unsigned long guess;

    for (int i = 0; i < 4; i++) {
        printf("guess %d: ", i);
        scanf("%p", &guess);
        if (*(addrs[i]) != guess) {
            printf("gg next time\n");
            exit(1);
        }
    }

    system("cat flag.txt");
}
