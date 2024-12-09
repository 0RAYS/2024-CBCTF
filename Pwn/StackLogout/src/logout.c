#include <stdio.h>
#include <string.h>

extern void who(char *buf, unsigned long size);

void logout(void) {
    char buf[0x40];
    puts("Who is logging out?");
input:
    printf("Input user: ");
    who(buf, 0x30);
    register char *newline;
    if ((newline = strchr(buf, '\n')))
        *newline = '\0';
    printf("Is this you? %s [y/n] ", buf);
    register char response = getchar();
    getchar(); // discard '\n'
    if (response != 'y')
        goto input;
    puts("logout");
}

