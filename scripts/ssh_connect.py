#!usr/bin/python3

from pexpect import pxssh
import time

import color 


def connect(ip, user, passwd):
	fail = 0

	try:
		ssh = pxssh.pxssh() # ssh connection setup
		ssh.login(ip, user, passwd) # cred login
		print(color.color_obj.Cyan+'''
[+] Credentials Found:''',  user+':'+passwd+'\n'+color.color_obj.ENDC)

		return ssh

	except KeyboardInterrupt:
		print(color.color_obj.RED+"\n\n[-] User interrupted with Keyboard"+color.color_obj.ENDC)
		exit(0)

	except Exception:
		if fail > 5:
			print(color.color_obj.RED+"[-] !!! To Many Socket Timeout"+color.color_obj.ENDC) 
			exit(0)
	    
		elif 'read_nonblocking' in str(Exception):
			fail += 1
			time.sleep(5)
			return connect(ip, user, passwd)
	    
		elif 'synchronize with original prompt' in str(Exception):
			time.sleep(1)
			return connect(ip, user, passwd)

	return None

#ip = input("Enter ip: ")
#user = input("Enter username: ")
#passwd = input("Enter passwd: ")

#conn = connect(ip, user, passwd)
