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
global pathChooseDescripts
global nums
global cursed
global cursetimer
global meteors
global meteortimer
global dragonTurn
global cursedTurn
pathChooseDescripts = ["You walk along the road, occasionally looking through the plants, ","You walk around the dead trees, the dry grass crunching under you feet. You look under a log, ","You walk toward the mountain. At the bottom, there is a small cave. You look in the cave, ","You walk up the hill. At the top, you look around, and see a big hole in the hill. You look inside, ","You walk into the trees, wandering through the darkness until you find a clearing, ","You walk through the swamp, occasionally stepping in puddles. You look behind a rock, ","You climb up the rocks, sometimes tripping over loose pebbles. You look behind a boulder, "]
pathdescripts = ["is green and lush with a small road.","has brown, dry grass littered with fallen trees.","leads toward a mountain that towers over the clouds.","leads toward a small hill in the distance.","wanders aimlessy through trees. The light fades as the trees grow thicker.","is hard to see as it is on very swampy ground and there are lots of big puddles that obscure the way.","is very rocky and there are points where you would have to scramble over boulders the size of a horse to find the next part."]
nums = ['1','2','3','4','5','6','7','8','9','0']
chances = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,4]
meteorchances = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]
chestchances = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,4]
choicelog = [0,0,0,0]

dragonTurn = False
cursedTurn = False
sword = False
shield = False
scroll = False
energy = 3
cursed = False
meteors = False
cursetimer = 0
meteortimer = 0
def askPath():
	global sword
	global shield
	global scroll
	global energy
	global nums
	isInNums = False
	x = 6
	n = [random.randint(0, x),random.randint(0, x),random.randint(0, x),random.randint(0, x),random.randint(0, x)]
	paths = random.randint(2, 5)
	
	print()
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
		choice = adds.getch()
		if type(choice) is bytes:
			choice = bytes.decode(choice)
		for i in nums:
			if choice == i:
				isInNums = True
				choiceint = int(choice)
				if choiceint <= paths:
					adds.pause()
					return [choiceint, n[choiceint-1]]
		if isInNums==False:
			print("That choice is invalid. Choose again.")
def findTreasure(n):
	global sword
	global shield
	global scroll
	global energy
	global pathChooseDescripts
	global cursed
	global meteors
	global meteorchances
	global dragonTurn
	global cursedTurn
	print(pathChooseDescripts[n])
	print()
	adds.pause()
	adds.pause()
	if meteors == True:
		out = random.choice(meteorchances)
	else:
		out = random.choice(chances)
	if (out == 1):
		print("but nothing is there.")
		energy = energy + 1
	elif (out == 2):
		print("and you find a chest.")
		graphics.draw("chestclosed")
		print("Press 'Y' to open, any other key to ignore.")
		ask = adds.getch()
		if type(ask) is bytes:
			ask = bytes.decode(ask)
		if ask == 'y':
			adds.pause()
			graphics.draw("chestopen")
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
			elif (chest == 4):
				cursed = True
				energy = energy - 5
				print("When you open the chest, a ghost comes out!")
				graphics.draw("ghost")
				print("You have been cursed! You lost 5 energy, and you will lose 2 energy every turn for 5 turns")
	elif (out == 3) and (dragonTurn == True):
		print("and a dragon comes out!")
		graphics.draw("dragon")
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
	elif (out == 3) and (dragonTurn == False):
		dragonTurn == True
		print("But nothing is there.")
		energy = energy+1
	elif (out == 4):
		meteors = True
		print("and you hear a noise.")
		print("Meteors are falling!!!")
		graphics.draw("meteor")
		print("Dragons appear much more often for 10 turns.")
	print("Press any key to continue.")
	y=adds.getch()
def kingDragon(n):
	global sword
	global shield
	global scroll
	global energy
	global pathChooseDescripts
	print(pathChooseDescripts[n])
	print()
	print("and you see a massive cave.")
	adds.pause()
	adds.pause()
	adds.pause()
	adds.pause()
	print("Press 'Y' to go in, any other key to bail.")
	y=adds.getch()
	if type(y) is bytes:
		y = bytes.decode(y)
	if y=='y':
		adds.clear()
		print("You enter the cave slowly, and you see a dark silhouette")
		adds.pause()
		adds.pause()
		adds.pause()
		print("Suddenly, the cave lights up! The dark silhouette was the Dragon King!")
		graphics.draw("kingdragon")
		adds.pause()
		if (sword == True) and (shield == True) and (energy >= 7):
			print("Having all of the equipment for the battle, you vanquish the Dragon King, but only after a long and intense battle.")
			graphics.showEnd("good")
		else:
			print("Since you did not come well equipped for the battle, the Dragon King easily burns you to a crisp.")
			graphics.showEnd("bad")

def main():
	global sword
	global shield
	global scroll
	global energy
	global choicelog
	global save
	global pathChooseDescripts
	global nums
	global cursed
	global cursetimer
	global meteors
	global meteortimer
	global cursedTurn
	graphics.showIntro()
	print("Press any key to continue.")
	y = adds.getch()
	while True:
	#	askLoad()
		while True:
			adds.clear()
			if (sword == True):
				print("You have a sword.")
				graphics.draw("sword")
			if (shield == True):
				print("You have a shield.")
				graphics.draw("shield")
			if (scroll == True):
				print("You have a scroll that says, \"Don't do 1-2-4-3\".")
				graphics.draw("scroll")
			if (cursed == True):
				print("You are cursed!!!")
				if cursedTurn == True:
					energy = energy - 2
				else:
					cursedTurn == True
				cursetimer = cursetimer + 1
				if cursetimer == 5:
					cursed = False
					cursetimer = 0
			if (meteors == True):
				print("Meteors are falling!!!")
				meteortimer = meteortimer + 1
				if meteortimer == 10:
					meteors = False
					meteortimer = 0
			print("You have",energy,"energy.")
			if (energy <= 0):
				print("You drop dead of exhaustion.")
				graphics.showEnd("bad")
			
			path = askPath()
			choicelog[0] = choicelog[1]
			choicelog[1] = choicelog[2]
			choicelog[2] = choicelog[3]
			choicelog[3] = path[0]

			if (choicelog == [1,2,4,3]) and (scroll == 1):
				kingDragon(path[1])
			findTreasure(path[1])
