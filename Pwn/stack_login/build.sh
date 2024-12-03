#!/bin/bash
set -e

docker-compose up -d || docker compose up -d

imageid=$(docker ps -n 1 -q)
cd attachment
docker cp ${imageid}:/home/ctf/pwn .
echo "copy file and generate attachment success!"