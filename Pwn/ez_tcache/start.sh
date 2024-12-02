#!/bin/bash
# Add your startup script
if [ ! $DASFLAG ];then
 echo CBCTF{TEST_FLAG}|tee /home/ctf/flag
else
 echo $DASFLAG|tee /home/ctf/flag 
fi
chown root:ctf /home/ctf/flag 
chmod 740 /home/ctf/flag

# DO NOT DELETE
/etc/init.d/xinetd start;
sleep infinity;