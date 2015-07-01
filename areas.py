import adds
def select(num):
	if (num == 1):
		road()
	elif (num == 2):
		trees()
	elif (num == 3):
		mountain()
	elif (num == 4):
		hill()
	elif (num == 5):
		forest()
	elif (num == 6):
		swamp()
	elif (num == 7):
		rocks()
def forest():
	adds.clear()
	print("==============THE=FOREST=============")
	print("As you walk through the forest, the continually fades, until there is pitch blackness.")
	print("Suddenly, there is a light up a head. It is a clearing in the forest.")
	print("Use 1, 2, 3, and 4 to go through the paths in the forest.")
def road():
	pass
def trees():
	pass
def mountain():
	pass
def hill():
	pass
def swamp():
	pass
def rocks():
	pass
gameMap = {"1,1":["1,5","5,1","2,1","2,2"]}
