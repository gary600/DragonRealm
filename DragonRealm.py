import random
import os
import pickle
#Getch() Import
# Getch for Linux, processes the key inputs
# by louis on StackOverflow
import time
def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch

getch = _find_getch()
#Actual Game
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
clear = lambda: os.system('clear')
sword = 0
shield = 0
scroll = 0
energy = 5
savew = open("DragonRealm-data/save.p", "wb")
savel = open("DragonRealm-data/save.p", "rb")
def pause():
	time.sleep(0.1)
def longpause():
	time.sleep(2)
def displayIntro():
	print("                                              /--------------\\")
	pause()
	print("==============================================|-DRAGON REALM-|===============================================")
	pause()
	print("                                              |by Gary Bailey|")
	pause()
	print("                                              \--------------/")
	pause()
	print("   You are a valiant knight who has been sent on a quest by the Monarch to destroy the wicked Dragon King.")
	pause()
	print("   You must choose which paths to follow. Some may bring you to the King, some may give you weapons...")
	pause()
	print("                              ...but others may send you to your death.")
	pause()
	print("              You must choose wisely, for the fate of the entire kingdom lies in your hands...")
	pause()
	print("=============================================================================================================")
	pause()
def showEnd(ending):
	global sword
	global shield
	global scroll
	global energy
	global choicelog
	print("===========================================================================================================================")
	pause()
	print("                  /------------------------\  /-\           /-\  /---------------\\")
	pause()
	print("                  \----------\  /----------/  | |           | |  |  -------------/")
	pause()
	print("                             |  |             | |           | |  | /")
	pause()
	print("                             |  |             | \           / |  | \\")
	pause()
	print("                             |  |             |  -----------  |  |  ---------\\")
	pause()
	print("                             |  |             |  -----------  |  |  ---------/")
	pause()
	print("                             |  |             | /           \ |  | /")
	pause()
	print("                             |  |             | |           | |  | \\")
	pause()
	print("                             |  |             | |           | |  |  -------------\\")
	pause()
	print("                             \--/             \-/           \-/  \---------------/")
	pause()
	print()
	pause()
	print("                           /---------------\      /-\      /-\       /-\\")
	pause()
	print("                           |  -------------/      |  \     | |       |  \\")
	pause()
	print("                           | /                    | \ \    | |       |   \\")
	pause()
	print("                           | \                    | |\ \   | |       | |\ \\")
	pause()
	print("                           |  ---------\          | | \ \  | |       | | \ \\")
	pause()
	print("                           |  ---------/          | |  \ \ | |       | | / /")
	pause()
	print("                           | /                    | |   \ \| |       | |/ /")
	pause()
	print("                           | \                    | |    \ \ |       |   /")
	pause()
	print("                           |  -------------\      | |     \  |       |  /")
	pause()
	print("                           \---------------/      \-/      \-/       \-/")
	pause()
	print()
	if (ending == "bad"):
		pause()
		print("            When he got the news of the failiure of your quest, the Monarch feared for his and each of his kingdom's")
		pause()
		print("            inhabitants' lives. The Dragon King noticed the deed of his servant and promoted him to Deputy, and then")
		pause()
		print("                                     the dragons invaded and fried the kingdom.")
		pause()
		print("                                               *sad trombone*")
	elif (ending == "good"):
		pause()
		print("            After vanquishing the Dragon King, you return to the kingdom. The monarch is pleased, for there would be")
		pause()
		print("                                        no more people being spontaneously eaten.")
	print()
	print("Would you like to try again? (y or n)")
	option = getch()
	if (option == 'y'):
		choicelog = [0,0,0,0]
		sword = 0
		shield = 0
		scroll = 0
		energy = 5
	else:
		raise SystemExit
def askLoad():
	global save
	global sword
	global shield
	global scroll
	global energy
	global choicelog
	print("Would you like to load a previous save file? (y or n)")
	saveChoice = getch()
	pause()
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
		pause()
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
	pause()
	pause()
	pause()
	pause()
	print("Press any key to continue.")
	y=getch()
	clear()
	print("You enter the cave slowly, and you see a dark silhouette")
	pause()
	pause()
	pause()
	print("Suddenly, the cave lights up! The dark silhouette was the Dragon King!")
	pause()
	if (sword == 1) and (shield == 1) and (energy >= 7):
		print("Having all of the equipment for the battle, you vanquish the Dragon King, but only after a long and intense battle.")
		showEnd("good")
	else:
		print("Since you did not come well equiped for the battle, the Dragon King easily burns you to a crisp.")
		showEnd("bad")
def askPath():
	global sword
	global shield
	global scroll
	global energy
	x = 6
	n = [random.randint(0, x),random.randint(0, x),random.randint(0, x),random.randint(0, x),random.randint(0, x)]
	paths = random.randint(2, 5)
	clear()
	print()
	if (sword == 1):
		print("You have a sword.")
	if (shield == 1):
		print("You have a shield.")
	if (scroll == 1):
		print("You have a scroll that says, \"Don't do 1-2-4-3\".")
	print("You have",energy,"energy.")
	print()
	pathdesc = pathdescripts[1]
	print("There are", paths, "paths.")
	pause()
	print("The first", pathdesc)
	pause()
	pathdesc = pathdescripts[n[1]]
	print("The second", pathdesc)
	pause()
	pathdesc = pathdescripts[n[2]]
	if (paths >= 3):
		
		print("The third", pathdesc)
		pathdesc = pathdescripts[n[3]]
	if (paths >= 4):
		pause()
		print("The fourth", pathdesc)
		pathdesc = pathdescripts[n[4]]
	if (paths >= 5):
		pause()
		print("The fifth", pathdesc)
		pause()
		print()
	print("Which path do you choose, out of the", paths,"?")
	print()
	while (True):
		choiceraw = getch()
		choice = int(choiceraw)
		if (choice >= 1) and (choice <= paths):
			pause()
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
	pause()
	pause()
	out = random.choice(chances)
	if (out == 1):
		print("but nothing is there.")
		energy = energy + 1
	elif (out == 2):
		print("and you find a chest.")
		pause()
		chest = random.choice(chestchances)
		if (chest == 1):
			sword = 1
			print("You found a sword! Now you can actually attack the Dragon King, or defend yourself against other dragons.")
			print("   /\\")
			print("   ||")
			print("   ||")
			print("   ||")
			print("   ||")
			print("   ||")
			print("|==||==|")
			print("   ||")
			print("   ||")
			print("  (==)")
		elif (chest == 2):
			shield = 1
			print("You found a fireproof shield! Now you can defend against enemy attacks, including a dragon's flame breath.")
			print("/----\\")
			print("|****|")
			print("\----/")
		elif (chest == 3):
			scroll = 1
			print("Inside the chest is a mysterious scroll. You unravel it:")
			print('''
			------------
			| don't do |
			|  1-2-4-3 |
			|and always|
			|trust a   |
			|scroll... |
			------------
			''')
			print("The parchment is splotted with blood. You roll it up and put it in your pocket.")
	elif (out == 3):
		print("and a dragon comes out!")
		pause()
		if (sword == 0) and (shield == 0):
			print("Having no sword or shield to defend yourself, the dragon fries you to a crisp.")
			pause()
			showEnd("bad")
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
	y=getch()
displayIntro()
while True:
#	askLoad()
	while True:
		if (energy <= 0):
			print("You drop dead of exhaustion.")
			showEnd("bad")
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