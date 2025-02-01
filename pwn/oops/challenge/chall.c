#include <stdlib.h>
#include <stdio.h>

// gcc oops.c -o oops -no-pie

void setup () {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
}

int main () {
	setup();

	printf("a gift from the author: %p\n", system);

	unsigned long number;
	printf("give me a number> ");
	scanf("%lu", &number);
	printf("You gave me: %lu\n", number);
	
	printf("give me another number> ");
	scanf("%lu", number); // oops
	printf("You gave me: %lu\n", number);
	
	
	puts("/bin/sh");


	return 0;
}
