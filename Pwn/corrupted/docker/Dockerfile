FROM ubuntu:latest

RUN sed -i 's@//.*archive.ubuntu.com@//mirrors.ustc.edu.cn@g' /etc/apt/sources.list.d/ubuntu.sources && \
    sed -i 's/security.ubuntu.com/mirrors.ustc.edu.cn/g'      /etc/apt/sources.list.d/ubuntu.sources
RUN apt update && apt upgrade -y
RUN apt install xinetd -y
RUN useradd -m ctf -s /bin/sh

WORKDIR /home/ctf
COPY ./corrupted .
COPY ./start.sh .
COPY ./ctf /etc/xinetd.d/

RUN chmod 755 ./corrupted

EXPOSE 1337
CMD ["./start.sh"]
