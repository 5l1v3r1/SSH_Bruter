#!usr/bin/python3

from pexpect import pxssh
import time

class Color:

	def __init__(self, GREEN, Blue, Cyan, Grey, RED, PURPLE, YEL, WHITE, ENDC, Default):

		self.GREEN = GREEN
		self.Blue = Blue
		self.Cyan = Cyan
		self.Grey =  Grey 
		self.RED = RED
		self.PURPLE = PURPLE
		self.YEL = YEL
		self.WHITE = WHITE
		self.ENDC = ENDC
		self.Default = Default



# For ssh login
def connect(ip, user, passwd):
	fail = 0

	try:
		ssh = pxssh.pxssh() # ssh connection setup
		ssh.login(ip, user, passwd) # cred login
		print(color_obj.Cyan+'''
[+] Credentials Found:''',  user+':'+passwd+'\n'+color_obj.ENDC)

		return ssh

	except KeyboardInterrupt:
		print(color_obj.RED+"\n\n[-] User interrupted with Keyboard"+color_obj.ENDC)
		exit(0)

	except Exception:
		if fail > 5:
			print(color_obj.RED+"[-] !!! To Many Socket Timeout"+color_obj.ENDC) 
			exit(0)
	    
		elif 'read_nonblocking' in str(Exception):
			fail += 1
			time.sleep(5)
			return connect(ip, user, passwd)
	    
		elif 'synchronize with original prompt' in str(Exception):
			time.sleep(1)
			return connect(ip, user, passwd)

	return None



# getting shell from the trgt machine
def shell_getting(user, ip, conn, startTime):
	if conn:

		totalTime = time.time() - startTime
		totalTime = '%.3f'%totalTime

		print(color_obj.PURPLE+f"\n[+] Process Completed\n[+] Time Taken : {totalTime}s\n"+color_obj.ENDC)

		print(color_obj.GREEN+'''[+] SSH connected!!, Type: exit to quit: 
		'''+color_obj.ENDC)

		command = input(user+'@'+ip+':$ ')
		while command != 'exit':
			conn.sendline(command)
			conn.prompt()
			print(conn.before.decode("utf-8"))
			command = input(user+'@'+ip+':$ ')
			
		else:
			print(color_obj.YEL+'''
Bye!
			'''+color_obj.ENDC)
		exit(0)




#ip = input("Enter ip: ")
#user = input("Enter username: ")
#passwd = input("Enter passwd: ")

#conn = connect(ip, user, passwd)

color_obj = Color('\033[92m', '\033[94m', '\033[96m', '\033[90m', '\033[91m', '\033[95m', '\033[93m', '\033[37m', '\033[0m', '\033[99m')


#print(color_obj.RED+"RED"+color_obj.ENDC)
