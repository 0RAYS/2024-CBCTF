#!/bin/bash
set -e

cp -r ../attachment/ .
docker-compose up -d || docker compose up -d
rm -r attachment/

imageid=$(docker ps -n 1 -q)

cd ../attachment
docker cp ${imageid}:/home/ctf/pwn .
docker cp -L ${imageid}:/lib/x86_64-linux-gnu/libc.so.6 .
docker cp -L ${imageid}:/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2 .
docker cp -L ${imageid}:/lib/x86_64-linux-gnu/libseccomp.so.2 .

echo "copy file and generate attachment success!"
