FROM ubuntu:noble-20240423

RUN sed -i 's@//.*archive.ubuntu.com@//mirrors.ustc.edu.cn@g' /etc/apt/sources.list.d/ubuntu.sources && \
    sed -i 's/security.ubuntu.com/mirrors.ustc.edu.cn/g'      /etc/apt/sources.list.d/ubuntu.sources
RUN apt-mark hold libc6
RUN apt update && apt upgrade -y
RUN apt install xinetd gdbserver -y
RUN useradd -m ctf -s /bin/sh

WORKDIR /home/ctf
COPY ./StackLogout .
COPY ./start.sh .
COPY ./ctf ./debug /etc/xinetd.d/

RUN chmod 755 ./StackLogout

EXPOSE 2049 3073 4097
CMD ["./start.sh"]
