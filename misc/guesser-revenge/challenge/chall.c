#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main (int argc, char *argv[]) {
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);

	char secret[32];
	char guess[32];
	int rfd = open("/dev/urandom", 0x0);
	read(rfd, secret, 32);

	printf("guess: ");
	read(0, guess, 32);
	if (memcmp(secret, guess, 32) == 0) {
		system("cat flag.txt");
	} else {
		execvp(argv[0], argv);
	}
	
}
