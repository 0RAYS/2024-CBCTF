#!/bin/bash
echo FLAG{TEST_FLAG}|tee /home/ctf/flag
chown root:ctf /home/ctf/flag 
chmod 740 /home/ctf/flag

/etc/init.d/xinetd start;
sleep infinity;