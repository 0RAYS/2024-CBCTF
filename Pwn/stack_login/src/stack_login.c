#include <stdio.h>
#include <unistd.h>

void gadget()
{
    __asm__ volatile("pop %rdx; ret");
}

void Init()
{
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void myread(char* buf, int size)
{
    for(int i = 0; i <= size; i++)
    {
        read(0, buf + i, 1);
        if (buf[i] == '\n')
        {
            buf[i] = '\0';
            break;
        }
    }
}

void Password()
{
    char password[0xe8];
    long pwdsize = sizeof(password);

    puts("enter your new password");
    myread(password, pwdsize);
    puts("confirm your new password");
    myread(password, pwdsize - 9);
}

char username[0xe8];
int namesize = sizeof(username);

int main()
{
    char padding[0x10];

    Init();

    puts("enter your username");
    myread(username, namesize);

    Password();
}