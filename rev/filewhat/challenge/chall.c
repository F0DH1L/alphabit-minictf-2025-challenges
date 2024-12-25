#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char buf[32];
int main(int argc, char* argv[], char* envp[]){
        if(argc<2){
                printf("Give me a number \n");
                return 0;
        }
        int fd = atoi( argv[1] )*5 ;
        int len = read(fd, buf, 32);
        if(!strcmp("ALPHABIT\n", buf)){
                system("/bin/cat flag.txt");
                exit(0);
        }
        return 0;
}
