#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

// gcc uaf.c -o uaf
// use glibc 2.35 with this chall
// hint: https://ir0nstone.gitbook.io/notes/binexp/heap/tcache-keys



struct account_t {
	char name[8];
	unsigned long amount;
};

struct account_t* account = NULL;


unsigned int menu() {
	unsigned int choice;
	puts("1- make account\n2- add amount\n3- delete account\n4- get flag");
	printf("> ");
	scanf("%u", &choice);
	return choice;
}

int main () {
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);

	puts("welcome to The BANK!");

	while (1) {
		unsigned int choice = menu();
		if (choice == 1) {
			if (account != NULL) {
				puts("you can't do that");
				exit(1);
			}
			account = malloc(sizeof(struct account_t));
			account->amount = 0;
			printf("name: ");
			read(0, account->name, 0x8);
		} else if (choice == 2) {
			if (account == NULL) {
				puts("you can't do that");
				exit(1);
			}
			account->amount = account->amount + 10;
		} else if (choice == 3) {
			free(account);
		} else if (choice == 4) {
			if (account->amount > 0xffffffffff) {
				system("cat flag.txt");
			} else {
				puts("you're poor, i can't give you the flag");
			}

		}
	}



}
