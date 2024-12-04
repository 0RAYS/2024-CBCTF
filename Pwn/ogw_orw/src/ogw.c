#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <seccomp.h>

void init()
{
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    puts("welcome to ogw challenge");
    puts("i believe you heard orw");
    puts("but what about ogw?");
    puts("trust me it's not so hard");
    puts("search ogw on the internet and you will know!\n");
}

void sandbox()
{
    // 创建一个默认的seccomp过滤器
    scmp_filter_ctx ctx = seccomp_init(SCMP_ACT_ALLOW); // 默认允许所有系统调用

    // 阻止execve系统调用
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execve), 0);
    // 阻止execveat系统调用
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execveat), 0);
    // 加载过滤器
    seccomp_load(ctx);
    // 释放过滤器
    seccomp_release(ctx);
}

void changeflag()
{
    puts("tell you a secret, flagname is changed");
    puts("try ogw to get flag name and then orw");
    puts("also, i will use sandbox to prevent you from getting shell");
    puts("so ogw and orw is your only way");
    puts("PS: flag is in /");
    printf("and, here is your gift:%p\n", &printf);
}

int main()
{
    char buf[0x10];

    init();

    changeflag();

    sandbox();

    read(0, buf, 0x200);
}