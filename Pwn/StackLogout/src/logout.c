#include <stdio.h>
#include <string.h>

extern void who(char *buf, unsigned size);

void logout(void) {
    char buf[0x130];
    puts("Who is logging out?");
input:
    printf("Input user: ");
    who(buf, sizeof(buf));
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

