SRC = stack_login.c
CFLAGS = -fno-stack-protector -static -z now -z noexecstack -O0

all: pwn

pwn: $(SRC)
	gcc $(SRC) $(CFLAGS) -o pwn

pwn_debug: $(SRC)
	gcc $(SRC) $(CFLAGS) -o pwn -g

clean:
	rm -rf ./pwn
