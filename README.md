# revshell-generator
<p align="center">
	<img src="http://www.hackthebox.eu/badge/image/234811" alt="Hack The Box">
</p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/insidious-security/reverse-shell-generator.svg?style=for-the-badge">
</p>

This python script creates a bash script called 'rev' listening with several interpreters for an incoming tcp connection:
- bash
- php
- netcat


## Usage:
```bash
# Example ip:
python3 revsh.py 10.0.0.x 4444

# This script is based on the revshell generator used by XCT in his CTF challenges.
# Since I could not find the source in his github repos, I wrote the above code instead.
```



