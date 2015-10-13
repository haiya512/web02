#!/usr/bin/env python
import os
cmd = "snmpwalk -v 2c 192.168.0.232 -c public .1.3.6.1.2.1.25.3.3.1.2|wc -l"
print os.popen(cmd).read().strip()
cmd1 = "snmpwalk -v2c -c public 192.168.0.232 1.3.6.1.2.1.2.1.0 | awk '{print $NF}'"
print os.popen(cmd1).read()
cmd2 = "snmpwalk -v2c -c public 192.168.0.232 .1.3.6.1.4.1.2021.4.3 | awk '{print $4}'"
print int(os.popen(cmd2).read())/1024
cmd3 = "snmpwalk -v2c -c public 192.168.0.232 .1.3.6.1.4.1.2021.4.3.6 | awk '{print $4}'"
print int(os.popen(cmd3).read())/1024
snmpwalk -v2c -c public 192.168.0.232 1.3.6.1.2.1.25.1.1 | awk '{print $5}'
