#!/usr/bin/python3

import progressbar
from time import sleep
import os


# Getting size of a file:

#file = "wordlist_test.txt"

#file_stats = os.stat(file)

#print(file_stats.st_size) # total size of file in bytes


def p_bar():
	widgets = ['bruteforcing:\r', progressbar.AnimatedMarker()]
	bar = progressbar.ProgressBar(widgets=widgets).start()
	
	for i in range(50): 
		sleep(0.09)
		bar.update(i)

#p_bar()
#print("Done")
