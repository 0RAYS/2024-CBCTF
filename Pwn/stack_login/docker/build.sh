#!/bin/bash
set -e

cp -r ../attachment/ .
docker-compose up -d || docker compose up -d
rm -r attachment/

cd ../attachment
imageid=$(docker ps -n 1 -q)
docker cp ${imageid}:/home/ctf/pwn .
echo "copy file and generate attachment success!"