#include <iconv.h>
#include <stdio.h>

extern void who(char *buf, unsigned size);

void getUserName(void) {
    char buf[0x100];
    who(buf, sizeof(buf));
}

int main(void) {
    puts("Since you have logged in, it's time to logout!!");
    getUserName();
}
