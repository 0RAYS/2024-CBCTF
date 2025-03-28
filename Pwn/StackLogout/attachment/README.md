# StackLogout 做题指南

由于这道题涉及cve复现，so会动态载入，而不是写死在elf中，因此简单的patch并不能成功复现
（即bug不在libc.so.6中），所以直接提供了docker文件，构建后开放3个端口即可方便调试。
给了libc主要是方便用pwntools找符号。

由于本题对库函数有要求，不能受cpuid影响，因此需要用一个固定偏移来计算所要跳转的函数，
因此如果不patchelf，大概率无法正常运行，如果需要本地运行，请先patchelf！
patchelf后，虽然不能成功复现cve，但是可以实现信息泄露。主系统使用ubuntu等系统库位置在
`/usr/lib/x86_64-linux-gnu/` 的选手可能能够成功打开iconv，其他系统无法打开iconv。

## 启动 docker

```sh
docker build docker/ -t stacklogout:latest
docker run -p 2049:2049 -p 3073:3073 -p 4097:4097 stacklogout:latest
```

## 本地连接服务

```python
EXE = './docker/StackLogout'
# io = process(EXE)
io = remote('127.0.0.1', 2049)
```

## 本地调试服务

```python
# io = process(EXE)
# gdb.attach(io)
io = remote('127.0.0.1', 3073) # 注意端口号变了
gdb.attach(('127.0.0.1', 4097), 'b *who+387', EXE)
```

attach上去后会停在`_start`的地方， **需要手动继续才能运行**
