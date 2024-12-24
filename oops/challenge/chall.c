#include <stdlib.h>
#include <stdio.h>

// gcc oops.c -o oops -no-pie


int main () {
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
