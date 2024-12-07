#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>

void* heap_list[0x10];

void init()
{
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    puts("welcome to ez_tcache");
    puts("you can see it's a tcache heap challenge");
    puts("i hope this will guide you to start the heapPwn");
    puts("this will use 2.27 libc");
    puts("the latest tcachebin attack is basicly the same thing");
}

void Add()
{
    puts("the index?");
    short index;
    read(0, &index, 2);
    heap_list[index] = malloc(0x80);
    puts("success");
}

void Delete()
{
    puts("the index?");
    short index;
    read(0, &index, 2);
    free(heap_list[index]);
    puts("success");
}

void Edit()
{
    puts("the index?");
    short index;
    read(0, &index, 2);
    puts("input content");
    read(0, heap_list[index], 0x80);
    puts("success");
}

void Gift()
{
    puts("because libc_address dones't exist in tcachebin");
    printf("here is one gift for you:%p\n", &printf);
    puts("also, some useful gdb command:vmmap, vis, bins, heap");
}

int main()
{
    init();

    while(true)
    {
        puts("input your choice");
        char choice = 0;
        read(0, &choice, 1);
        switch (choice)
        {
        case 1:
            Add();
            break;
        case 2:
            Delete();
            break;
        case 3:
            Edit();
            break;
        case 4:
            Gift();
            break;
        default:
            puts("please input number between 1-4");
            break;
        }
    }
}