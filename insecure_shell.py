#!/usr/bin/python3

import pyfiglet

bann = pyfiglet.figlet_format("Insecure Shell", font = "slant")
print(bann)
print('''Please feel free to reach me for some suggestions:

⚪ https://www.linkedin.com/in/reveng007/

⚪ https://twitter.com/soumyani1
''')

GREEN = '\033[92m'
Blue = '\033[94m'
Cyan = '\033[96m'
Magenta = '\033[95m'
Grey = '\033[90m'
Black = '\033[90m'
RED = '\033[91m'
PURPLE = '\033[95m'
YEL = '\033[93m'
WHITE = '\033[37m'
ENDC = '\033[0m'
Default = '\033[99m'


Enquire = input(GREEN+'''

What do you want to bruteforce??

1. Bruteforce ssh password
2. Bruteforce ssh user
3. Bruteforce both creds of ssh
4. Whole Summary

: '''+ENDC)

print(Enquire)


if (Enquire == "1"):
	print('''

usage: ssh_brute-pass.py [-h] ip user file port

positional arguments:
  ip          Specify Target ip
  user        Specify Target User
  file        Specify Wordlist
  port        Port Number

optional arguments:
  -h, --help  show this help message and exit

''')

elif (Enquire == "2"):
	print('''

usage: ssh_brute-user.py [-h] ip file passwd port

positional arguments:
  ip          Specify Target ip
  file        Specify Wordlist
  passwd      Specify password
  port        Port Number

optional arguments:
  -h, --help  show this help message and exit
 ''')

elif (Enquire == "3"):
	print('''

usage: ssh_brute-both.py [-h] ip file1 file2 port

positional arguments:
  ip          Specify Target ip
  file1       Specify Wordlist
  file2       Specify Wordlist
  port        Port Number

optional arguments:
  -h, --help  show this help message and exit
 ''')

elif (Enquire == "4"):
	print('''

+ ---       ---------     --- +
For only password bruteforcing:
+ ---       ---------     --- +

usage: ssh_brute-pass.py [-h] ip user file port

positional arguments:
  ip          Specify Target ip
  user        Specify Target User
  file        Specify Wordlist
  port        Port Number

optional arguments:
  -h, --help  show this help message and exit

+ ---   ----------    --- +
For only user bruteforcing:
+ ---   ----------    --- +

usage: ssh_brute-user.py [-h] ip file passwd port

positional arguments:
  ip          Specify Target ip
  file        Specify Wordlist
  passwd      Specify password
  port        Port Number

optional arguments:
  -h, --help  show this help message and exit

+ -----       ----------   ----- +
For bruteforcing both credentials:
+ -----       ----------   ----- +

usage: ssh_brute-both.py [-h] ip file1 file2 port

positional arguments:
  ip          Specify Target ip
  file1       Specify Wordlist
  file2       Specify Wordlist
  port        Port Number

optional arguments:
  -h, --help  show this help message and exit

''')


elif ((Enquire != 1) or (Enquire != 2) or (Enquire != 3)):
	print(RED+'''
[-] Please Choose from 1, 2 and 3
'''+ENDC)
	exit(0)

