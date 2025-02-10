#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h> 

char buf[32];
int main(){
        setbuf(stdin, 0);
        setbuf(stdout, 0);
        setbuf(stderr, 0);
        int x;
        printf("Give me a number : ");
        scanf("%d",&x) ;
        int fd = (x*5)%2 ;
        int len = read(fd, buf, 32);
        if(!strcmp("ALPHABIT", buf)){
                system("/bin/cat flag.txt");
                exit(0);
        }
        return 0;
}
