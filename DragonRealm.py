import random
import os
import pickle
import graphics
import adds
global sword
global shield
global scroll
global energy
global choicelog
global save
pathdescripts = ["is green and lush with a small road.","has brown, dry grass littered with fallen trees.","leads toward a mountain that towers over the clouds.","leads toward a small hill in the distance.","wanders aimlessy through trees. The light fades as the trees grow thicker.","is hard to see as it is on very swampy ground and there are lots of big puddles that obscure the way.","is very rocky and there are points where you would have to scramble over boulders the size of a horse to find the  next part."]
nums = ["1","2","3","4","5","6","7","8","9","0"]
chances = [1,1,1,1,1,1,1,2,2,2,3]
chestchances = [1,1,2,2,3]
choicelog = [0,0,0,0]

sword = 0
shield = 0
scroll = 0
energy = 5

def askLoad():
	global save
	global sword
	global shield
	global scroll
	global energy
	global choicelog
	print("Would you like to load a previous save file? (y or n)")
	saveChoice = adds.getch()
	adds.pause()
	if (saveChoice == 'y'):
		with open("DragonRealm-data/save.p", "rb") as infile:
			x = pickle.load(infile)
			infile.close()
		sword = x[0]
		shield = x[1]
		scroll = x[2]
		energy = x[3]
	else:
		print("Starting new game")
		adds.pause()
def kingDragon(n):
	global sword
	global shield
	global scroll
	global energy
	if (n == 0):
		print("You walk along the road, occasionally looking through the plants, ")
	elif (n == 1):
		print("You walk around the dead trees, the dry grass crunching under you feet. You look under a log, ")
	elif (n == 2):
		print("You walk toward the mountain. At the bottom, there is a small cave. You look in the cave, ")
	elif (n == 3):
		print("You walk up the hill. At the top, you look around, and see a big hole in the hill. You look inside, ")
	elif (n == 4):
		print("You walk into the trees, wandering through the darkness until you find a clearing, ")
	elif (n == 5):
		print("You walk through the swamp, occasionally stepping in puddles. You look behind a rock, ")
	elif (n == 6):
		print("You climb up the rocks, sometimes tripping over loose pebbles. You look behind a boulder, ")
	print()
	print("and you see a massive cave.")
	adds.pause()
	adds.pause()
	adds.pause()
	adds.pause()
	print("Press any key to continue.")
	y=adds.getch()
	adds.clear()
	print("You enter the cave slowly, and you see a dark silhouette")
	adds.pause()
	adds.pause()
	adds.pause()
	print("Suddenly, the cave lights up! The dark silhouette was the Dragon King!")
	adds.pause()
	if (sword == 1) and (shield == 1) and (energy >= 7):
		print("Having all of the equipment for the battle, you vanquish the Dragon King, but only after a long and intense battle.")
		graphics.showEnd("good")
	else:
		print("Since you did not come well equiped for the battle, the Dragon King easily burns you to a crisp.")
		graphics.showEnd("bad")
def askPath():
	global sword
	global shield
	global scroll
	global energy
	x = 6
	n = [random.randint(0, x),random.randint(0, x),random.randint(0, x),random.randint(0, x),random.randint(0, x)]
	paths = random.randint(2, 5)
	
	adds.clear()
	print()
	if (sword == 1):
		print("You have a sword.")
		graphics.draw("sword")
	if (shield == 1):
		print("You have a shield.")
		graphics.draw("shield")
	if (scroll == 1):
		print("You have a scroll that says, \"Don't do 1-2-4-3\".")
		graphics.draw("scroll")
	print("You have",energy,"energy.")
	print()
	pathdesc = pathdescripts[1]
	print("There are", paths, "paths.")
	adds.pause()
	print("The first", pathdesc)
	adds.pause()
	pathdesc = pathdescripts[n[1]]
	print("The second", pathdesc)
	adds.pause()
	pathdesc = pathdescripts[n[2]]
	if (paths >= 3):
		
		print("The third", pathdesc)
		pathdesc = pathdescripts[n[3]]
	if (paths >= 4):
		adds.pause()
		print("The fourth", pathdesc)
		pathdesc = pathdescripts[n[4]]
	if (paths >= 5):
		adds.pause()
		print("The fifth", pathdesc)
		adds.pause()
		print()
	print("Which path do you choose, out of the", paths,"?")
	print()
	while (True):
		choiceraw = adds.getch()
		choice = int(choiceraw)
		if (choice >= 1) and (choice <= paths):
			adds.pause()
			return [choice, n[choice-1]]
		else:
			print("That choice is invalid. Choose again")
def findTreasure(n):
	global sword
	global shield
	global scroll
	global energy
	if (n == 0):
		print("You walk along the road, occasionally looking through the plants, ")
	elif (n == 1):
		print("You walk around the dead trees, the dry grass crunching under you feet. You look under a log, ")
	elif (n == 2):
		print("You walk toward the mountain. At the bottom, there is a small cave. You look in the cave, ")
	elif (n == 3):
		print("You walk up the hill. At the top, you look around, and see a big hole in the hill. You look inside, ")
	elif (n == 4):
		print("You walk into the trees, wandering through the darkness until you find a clearing, ")
	elif (n == 5):
		print("You walk through the swamp, occasionally stepping in puddles. You look behind a rock, ")
	elif (n == 6):
		print("You climb up the rocks, sometimes tripping over loose pebbles. You look behind a boulder, ")
	print()
	adds.pause()
	adds.pause()
	out = random.choice(chances)
	if (out == 1):
		print("but nothing is there.")
		energy = energy + 1
	elif (out == 2):
		print("and you find a chest.")
		adds.pause()
		chest = random.choice(chestchances)
		if (chest == 1):
			sword = 1
			print("You found a sword! Now you can actually attack the Dragon King, or defend yourself against other dragons.")
			graphics.draw("sword")
		elif (chest == 2):
			shield = 1
			print("You found a fireproof shield! Now you can defend against enemy attacks, including a dragon's flame breath.")
			graphics.draw("shield")
		elif (chest == 3):
			scroll = 1
			print("Inside the chest is a mysterious scroll. You unravel it:")
			graphics.draw("scroll")
			print("The parchment is splotted with blood. You roll it up and put it in your pocket.")
	elif (out == 3):
		print("and a dragon comes out!")
		adds.pause()
		if (sword == 0) and (shield == 0):
			print("Having no sword or shield to defend yourself, the dragon fries you to a crisp.")
			adds.pause()
			graphics.showEnd("bad")
		elif (sword == 1) and (shield == 0):
			print("Since you have a sword to attack the dragon, but no shield, you won the battle but were thoroughly exhausted because you had to dodge every flame.")
			energy = energy - 6
		elif (sword == 0) and (shield == 1):
			print("Since you only have a shield, you couldn't attack the dragon, but you were able to flee. This tired you out, since you had to run so much.")
			energy = energy - 6
		elif (sword == 1) and (shield == 1):
			print("Since you have a sword and a shield, you were able to slay the dragon no problem. It only made you a little tired.")
			energy = energy - 3
	print("Press any key to continue.")
	y=adds.getch()
graphics.displayIntro()
print("Press any key to continue.")
y = adds.getch()
while True:
#	askLoad()
	while True:
		if (energy <= 0):
			print("You drop dead of exhaustion.")
			graphics.showEnd("bad")
		
		path = askPath()
		choicelog[0] = choicelog[1]
		choicelog[1] = choicelog[2]
		choicelog[2] = choicelog[3]
		choicelog[3] = path[0]
		print(choicelog)
		if (choicelog == [1,2,4,3]) and (scroll == 1):
			kingDragon(path[1])
		findTreasure(path[1])
		savestuff = (sword, shield, scroll, energy)
#		with (open("DragonRealm-data/save.p", "wb")) as outfile:
#			pickle.dump(savestuff, outfile)
#			outfile.close()
