#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/sha.h>
#include <sys/cdefs.h>

static long match[4];
static unsigned char randdata[32] = {};

__attribute__((constructor))
static void loadBuf(void) {
    FILE *random = fopen("/dev/random", "rb");
    if (!random) {
        puts("IO error: can not open device");
        exit(1);
    }
    register size_t readin = fread(randdata, 1, 32, random);
    if (readin != 32) {
        puts("IO error: can not read from device");
        exit(1);
    }
    fclose(random);
}

static unsigned long getLong(void) {
    char buf[32];
    buf[31] = '\0';
    fgets(buf, 31, stdin);
    return atol(buf);
}

static void inputNumber(int round) {
    printf("#%d QWORD:\n", round);
    printf("    Which QWORD do you want to write?\n    IDX > ");
    int idx = getLong();
    if (idx >= 4) {
        puts("Out-of-bound write detected!!");
        exit(1);
    }
    printf("    QWORD to write?\n    VAL > ");
    match[idx] = getLong();
}

__always_inline
static void printHex32(const char *msg, const unsigned char *buf) {
    printf("%s: ", msg);
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 8; j++)
            printf("%02hhx", buf[(i << 3) | j]);
        putchar(' ');
    }
    putchar('\n');
}

__attribute_noinline__
static int verify(void) {
    unsigned char buf[32];
    SHA256(randdata, 32, buf);
    printHex32("Original data", randdata);
    puts("               ->");
    printHex32("SHA256 digest", buf);
    puts("               ?=");
    printHex32("User's  input", (const unsigned char *)match);
    putchar('\n');
    int cmp = memcmp(buf, match, 32);
    return cmp ? 0 : 1;
}

int main(void) {
    setbuf(stdout, NULL);
    puts("This is a number guess program, you'll need to guess 32 bytes.");
    puts("8 bytes each time, so you will have 4 times to write!\n");
    for (int i = 0; i < 4; i++)
        inputNumber(i + 1);
    putchar('\n');
    puts("Now let's check if you're right!");
    switch (verify()) {
        case 1:
            puts("Congratulations!! You're so lucky today!!");
            break;
        case 0:
            puts("Sorry, that's not the case...");
            break;
        default:
            puts("Impossible...");
            exit(1);
    }
    return 0;
}
