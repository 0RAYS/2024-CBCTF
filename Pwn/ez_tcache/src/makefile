all: pwn

pwn: ez_tcache.c
	gcc -fstack-protector-all -pie -z now -z noexecstack -O0 ez_tcache.c -o pwn

pwn_debug: ez_tcache.c
	cp ../attachment/pwn .
	patchelf ./pwn --set-interpreter ../attachment/ld-linux-x86-64.so.2
	patchelf ./pwn --replace-needed libc.so.6 ../attachment/libc.so.6

clean:
	rm -rf ./pwn
	