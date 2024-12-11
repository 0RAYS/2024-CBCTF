#!/bin/bash
echo $FLAG > /home/ctf/flag
chown root:ctf /home/ctf/flag 
chmod 740 /home/ctf/flag

/etc/init.d/xinetd start;
sleep infinity;