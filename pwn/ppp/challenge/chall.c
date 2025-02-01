#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

// gcc chall.c -o chall -no-pie

void setup(){
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);
}

int main () {
	setup();

	printf("help from author: %p\n", printf);
	char buf[0x10];

	printf("data: ");
	read(0x0, buf, 0x30);
}
