#!/bin/bash
echo $FLAG > /home/ctf/flag

chown root:ctf /home/ctf/flag 
chmod 740 /home/ctf/flag

random_suffix=$(head -c 10 /dev/urandom | base64 | tr -dc 'a-zA-Z0-9' | head -c 10)

mv flag "flag${random_suffix}"

/etc/init.d/xinetd start;
sleep infinity;