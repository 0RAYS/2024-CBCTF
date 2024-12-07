SRC = ogw.c
CFLAGS = -fno-stack-protector -z now -z noexecstack -O0 -lseccomp

all: pwn

pwn: $(SRC)
	gcc $(SRC) $(CFLAGS) -o pwn
	# patchelf ./pwn --replace-needed libc.so.6 ./libc.so.6
	# patchelf ./pwn --set-interpreter ./ld-linux-x86-64.so.2
	# patchelf ./pwn --replace-needed libseccomp.so.2 ./libseccomp.so.2
	# cp pwn ../attachment

clean:
	rm -rf ./pwn
