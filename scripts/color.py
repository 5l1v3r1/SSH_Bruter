#!/usr/bin/python3

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

	def apply(self):

		print(self.GREEN+"Green"+self.ENDC)
		print(self.Blue+"Blue"+self.ENDC)
		print(self.Cyan+"Cyan"+self.ENDC)
		print(self.Grey+"Grey"+self.ENDC)
		print(self.RED+"RED"+self.ENDC)
		print(self.PURPLE+"PURPLE"+self.ENDC)
		print(self.YEL+"YEL"+self.ENDC)
		print(self.WHITE+"WHITE"+self.ENDC)
		print(self.Default+"Default"+self.Default)


color_obj = Color('\033[92m', '\033[94m', '\033[96m', '\033[90m', '\033[91m', '\033[95m', '\033[93m', '\033[37m', '\033[0m', '\033[99m')

#print(color_obj.RED+"RED"+color_obj.ENDC)

'''
def func(num):
	print(num)

num = int(input("Enter num: "))
f = func(num)
'''
