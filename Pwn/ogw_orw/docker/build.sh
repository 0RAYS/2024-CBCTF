#!/bin/bash
set -e

docker-compose up -d || docker compose up -d

imageid=$(docker ps -n 1 -q)

cd attachment
docker cp ${imageid}:/home/ctf/pwn .
docker cp -L ${imageid}:/lib/x86_64-linux-gnu/libc.so.6 .
docker cp -L ${imageid}:/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2 .
docker cp -L ${imageid}:/lib/x86_64-linux-gnu/libseccomp.so.2 .
patchelf ./pwn --replace-needed libc.so.6 ./libc.so.6
patchelf ./pwn --set-interpreter ./ld-linux-x86-64.so.2
patchelf ./pwn --replace-needed libseccomp.so.2 ./libseccomp.so.2

echo "copy file and generate attachment success!"
