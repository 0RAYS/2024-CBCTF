#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <sys/cdefs.h>
#include <unistd.h>

extern void logout(void);

static void pwnShell(void) {
    char cmd[0x60];
    cmd[sizeof(cmd) - 1] = '\0';
    bool exited = false;
    char *newline;
    while (!exited) {
        printf("psh> ");
        fgets(cmd, sizeof(cmd) - 1, stdin);
        if ((newline = strchr(cmd, '\n')))
            *newline = '\0';
#define STREQ(str) strstr(cmd, str) == cmd
        if (STREQ("logout") || STREQ("exit")) {
            logout();
            exited = true;
        } else if (STREQ("echo"))
            puts(cmd + 5);
        else if (STREQ("whoami"))
            puts("ctf");
        else if (STREQ("id"))
            puts("uid=1001(ctf) gid=1001(ctf) groups=1001(ctf)");
        else if (STREQ("cd"))
            chdir(cmd + 3);
        else if (STREQ("pwd")) {
            getcwd(cmd, sizeof(cmd) - 1);
            puts(cmd);
        } else if (cmd[0] != '\0')
            puts("Function not implemented!");
    }
}

int main(void) {
    setbuf(stdout, NULL);
    puts("You have logged in, enjoy my shell!");
    pwnShell();
    exit(0);
}
