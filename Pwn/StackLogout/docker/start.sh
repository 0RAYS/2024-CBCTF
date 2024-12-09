#!/bin/bash
if [[ "z${FLAG}z" == "zz" ]]; then
    FLAG="CBCTF{test_flag}"
fi
echo $FLAG > flag
echo $FLAG > /flag
chmod 644 flag /flag
unset FLAG

echo "Failed xinetd" > /etc/banner_fail

service xinetd start
sleep infinity
