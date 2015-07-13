import DragonRealm
import adds
def showIntro():
	print('''
                                                     /|\      ))_((     /|\\
                            (@)                     / | \    (/\|/\)   / | \                      (@)
                            |-| -------------------/--|-voV---\`|'/--Vov-|--\---------------------|-|
                            | |                         '^`   (o o)  '^`                          | |
                            |-|                               `\Y/'                               |-|
                            | |       ___  ____ ____ ____ ____ _  _ ____ ____ ____ _    _  _      | |
                            |-|       |  \ |__/ |__| | __ |  | |\ | |__/ |___ |__| |    |\/|      |-|
                            | |       |__/ |  \ |  | |__] |__| | \| |  \ |___ |  | |___ |  |      | |
                            |-|        by Gary B                                                  |-|
                            | |___________________________________________________________________| |
                            |-|/'            l   /\ /         ( (       \ /\   l                `\|-|
                            (@)              l /   V           \ \       V   \ l                  (@)
                                            l/                _) )_          \I
                                                              `\ /'
                                                                `
	''')
	adds.pause()
	print("   You are a valiant knight who has been sent on a quest by the Monarch to destroy the wicked Dragon King.")
	adds.pause()
	print("   You must choose which paths to follow. Some may bring you to the King, some may give you weapons...")
	adds.pause()
	print("                              ...but others may send you to your death.")
	adds.pause()
	print("              You must choose wisely, for the fate of the entire kingdom lies in your hands...")
	adds.pause()
	print("=============================================================================================================")
	adds.pause()
def showEnd(ending):
	global sword
	global shield
	global scroll
	global energy
	global choicelog
	print("====================================================================================================================")
	adds.pause()
	print("              _____                    _____                    _____           ")
	adds.pause()
	print("             /\    \                  /\    \                  /\    \  ")
	adds.pause()
	print("            /::\    \                /::\____\                /::\    \ ")
	adds.pause()
	print("            \:::\    \              /:::/    /               /::::\    \ ")
	adds.pause()
	print("             \:::\    \            /:::/    /               /::::::\    \ ")
	adds.pause()
	print("              \:::\    \          /:::/    /               /:::/\:::\    \ ")
	adds.pause()
	print("               \:::\    \        /:::/____/               /:::/__\:::\    \ ")
	adds.pause()
	print("               /::::\    \      /::::\    \              /::::\   \:::\    \ ")
	adds.pause()
	print("              /::::::\    \    /::::::\    \   _____    /::::::\   \:::\    \ ")
	adds.pause()
	print("             /:::/\:::\    \  /:::/\:::\    \ /\    \  /:::/\:::\   \:::\    \ ")
	adds.pause()
	print("            /:::/  \:::\____\/:::/  \:::\    /::\____\/:::/__\:::\   \:::\____\ ")
	adds.pause()
	print("           /:::/    \::/    /\::/    \:::\  /:::/    /\:::\   \:::\   \::/    /")
	adds.pause()
	print("          /:::/    / \/____/  \/____/ \:::\/:::/    /  \:::\   \:::\   \/____/ ")
	adds.pause()
	print("         /:::/    /                    \::::::/    /    \:::\   \:::\    \ ")
	adds.pause()
	print("        /:::/    /                      \::::/    /      \:::\   \:::\____\ ")
	adds.pause()
	print("        \::/    /                       /:::/    /        \:::\   \::/    /")
	adds.pause()
	print("         \/____/                       /:::/    /          \:::\   \/____/")
	adds.pause()
	print("                                      /:::/    /            \:::\    \  ")
	adds.pause()
	print("                                     /:::/    /              \:::\____\ ")
	adds.pause()
	print("                                     \::/    /                \::/    /")
	adds.pause()
	print("                                      \/____/                  \/____/ ")
	adds.pause()
	print("              _____                    _____                    _____          ")
	adds.pause()
	print("             /\    \                  /\    \                  /\    \      ")
	adds.pause()
	print("            /::\    \                /::\____\                /::\    \  ")
	adds.pause()
	print("           /::::\    \              /::::|   |               /::::\    \ ")
	adds.pause()
	print("          /::::::\    \            /:::::|   |              /::::::\    \ ")
	adds.pause()
	print("         /:::/\:::\    \          /::::::|   |             /:::/\:::\    \ ")
	adds.pause()
	print("        /:::/__\:::\    \        /:::/|::|   |            /:::/  \:::\    \ ")
	adds.pause()
	print("       /::::\   \:::\    \      /:::/ |::|   |           /:::/    \:::\    \ ")
	adds.pause()
	print("      /::::::\   \:::\    \    /:::/  |::|   | _____    /:::/    / \:::\    \ ")
	adds.pause()
	print("     /:::/\:::\   \:::\    \  /:::/   |::|   |/\    \  /:::/    /   \:::\ ___\ ")
	adds.pause()
	print("    /:::/__\:::\   \:::\____\/:: /    |::|   /::\____\/:::/____/     \:::|    |")
	adds.pause()
	print("    \:::\   \:::\   \::/    /\::/    /|::|  /:::/    /\:::\    \     /:::|____|")
	adds.pause()
	print("     \:::\   \:::\   \/____/  \/____/ |::| /:::/    /  \:::\    \   /:::/    /")
	adds.pause()
	print("      \:::\   \:::\    \              |::|/:::/    /    \:::\    \ /:::/    /")
	adds.pause()
	print("       \:::\   \:::\____\             |::::::/    /      \:::\    /:::/    / ")
	adds.pause()
	print("        \:::\   \::/    /             |:::::/    /        \:::\  /:::/    / ")
	adds.pause()
	print("         \:::\   \/____/              |::::/    /          \:::\/:::/    / ")
	adds.pause()
	print("          \:::\    \                  /:::/    /            \::::::/    / ")
	adds.pause()
	print("           \:::\____\                /:::/    /              \::::/    / ")
	adds.pause()
	print("            \::/    /                \::/    /                \::/____/")
	adds.pause()
	print("             \/____/                  \/____/                  ~~      ")
	adds.pause()
	print()
	if (ending == "bad"):
		adds.pause()
		print("         When he got the news of the failure of your quest, the Monarch feared for his and each of his kingdom's")
		adds.pause()
		print("         inhabitants' lives. The Dragon King noticed the deed of his servant and promoted him to Deputy, and then")
		adds.pause()
		print("                                  the dragons invaded and fried the kingdom.")
		adds.pause()
		print("                                            *sad trombone*")
	elif (ending == "good"):
		adds.pause()
		print("         After vanquishing the Dragon King, you return to the kingdom. The monarch is pleased, for there would be")
		adds.pause()
		print("                                     no more people being spontaneously eaten.")
		rollCredits()
	print("Press any key to exit")
	adds.getch()
	raise SystemExit
def draw(obj):
	if (obj == "sword"):
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
	elif (obj == "shield"):
		print("/----\\")
		print("|****|")
		print("\----/")
	elif (obj == "scroll"):
		print("------------")
		print("| don't do |")
		print("|  1-2-4-3 |")
		print("|and always|")
		print("|trust a   |")
		print("|scroll... |")
		print("------------")
	elif (obj == "chestopen"):
		print("""
    	              _.--.
                  _.-'_:-'||
              _.-'_.-::::'||
         _.-:'_.-::::::'  ||
       .'`-.-:::::::'     ||
      /.'`;|:::::::'      ||_
     ||   ||::::::'     _.;._'-._
     ||   ||:::::'  _.-!oo @.!-._'-.
     \'.  ||:::::.-!()oo @!()@.-'_.|
      '.'-;|:.-'.&$@.& ()$%-'o.'\\U||
        `>'-.!@%()@'@_%-'_.-o _.|'||
         ||-._'-.@.-'_.-' _.-o  |'||
         ||=[ '-._.-\\U/.-'    o |'||
         || '-.]=|| |'|      o  |'||
         ||      || |'|        _| ';
         ||      || |'|    _.-'_.-'
         |'-._   || |'|_.-'_.-'
          '-._'-.|| |' `_.-'
              '-.||_/.-'
""")
	elif (obj == "dragon"):
		print("""
<~>
 \ \,_____
       ___`\\ 
       \('>\`-__ 
         ~      ~~~--__            **              ***
               ______  (@\   *******  ****    *******    ******
              /******~~~~\|**********************************
      \       `--____******************************************
     / ~~~--_____    ~~~/ ***************************************
                 `~~~~~         ******************************
                                      ****    **************
                                        ***       ***********
                                                        ********
		""")
	elif (obj == "kingdragon"):
		print("""
		                                         __----~~~~~~~~~~~------___
                                      .  .   ~~//====......          __--~ ~~
                      -.            \_|//     |||\\  ~~~~~~::::... /~
                   ___-==_       _-~o~  \/    |||  \\            _/~~-
           __---~~~.==~||\=_    -_--~/_-~|-   |\\   \\        _/~
       _-~~     .=~    |  \\-_    '-~7  /-   /  ||    \      /
     .~       .~       |   \\ -_    /  /-   /   ||      \   /
    /  ____  /         |     \\ ~-_/  /|- _/   .||       \ /
    |~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\\
             '         ~-|      /|    |-~\~~       __--~~
                         |-~~-_/ |    |   ~\_   _-~            /\\
                              /  \     \__   \/~                \\__
                          _--~ _/ | .-~~____--~-/                  ~~==.
                         ((->/~   '.|||' -_|    ~~-/ ,              . _||
                                    -_     ~\      ~~---l__i__i__i--~~_/
                                    _-~-__   ~)  \--______________--~~
                                  //.-~~~-~_--~- |-------~~~~~~~~
                                         //.-~~~--\\
		""")
	elif (obj == "chestclosed"):
		print("""
          _,---.-.---------------.-.---,_
     _.-'`====/o/=================\o\====`'-._
   .'========/o/===================\o\========'.
  |---------)~(---------------------)~(---------|
   \________\o/________.---.________\o/________/
    |=======/o\========) ? (========/o\=======|
    |       | |       (  '  )       | |       |
    |=======|o|========'---'========|o|=======|
    |       | |         ____        | |       |
    |=======|o|========)X| /(=======|o|=======|
    |       | |       |XX|/ /|      | |       |
    |=======|o|=======\--/ / /======|o|=======|
    |       | |        '/_/.'       | |       |
    lc======|o|=====================|o|=======|
    '-------'-'---------------------'-'-------'
		""")
	elif (obj == "ghost"):
		print("""
                         .-.
                       .'   `.
                       :g g   :
                       : o    `.
                      :         ``.
                     :             `.
                    :  :         .   `.
                    :   :          ` . `.
                     `.. :            `. ``;
                        `:;             `:'
                           :              `.
                            `.              `.     .
                              `'`'`'`---..,___`;.-'
		""")
	elif (obj == "meteor"):
		print("""
		
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▀▀░▄█░░
░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄█▀▄▄▄▄██▀░░░
░░░░░░░░░░░░░░░▄▄▄▄▄▄▄████████░▄▄██░░░░░
░░░░░░░░░▄▄▀▀▀▀▄▄▄▄████████▀▄▄████░░░░░░
░░░░░░▄▀▀▄▄▄▀▀▀░▄██████████▀█▀██▀░░░░░░░
░░░░▄▀▄▀█▄█████████▄████▄▄██▄██░░░░░░░░░
░░▄▀▄▀▄██▀▄▄▄███▀▀▀█▄██▀███▀██░░░░░░░░░░
░▄▀█▄█▀▄▄▀███▄█░░░▄██████▀▄██░░░░░░░░░░░
▄▀██▀▄▀░▄█████████▀▀████████▀░░░░░░░░░░░
███▀█░▄████▀█▄▄▄█████▀█████░░░░░░░░░░░░░
█▀█▀▄██████▀▀▀████▀▀█████▀░░░░░░░░░░░░░░
███▄███▀░▄▄████████▀██▀░░░░░░░░░░░░░░░░░
░███▀█▄██████▀▄██▀▄▀█░░░░░░░░░░░░░░░░░░░
░▀█░███▄▄██▄▄██▄▀█▄▀░░░░░░░░░░░░░░░░░░░░
░░░▀▀██▄▄▄▄███▄▀▀░░░░░░░░░░░░░░░░░░░░░░░
		""")
def rollCredits():
	print("=========================================CREDITS============================================")
	adds.pause()
	print("GAME DESIGN: Gary B")
	adds.pause
	print("PROGRAMMING: Gary B")
	adds.pause()
	print("ART:")
	adds.pause()
	print("	Sword, Shield, Scroll: Gary B")
	adds.pause()
	print("	Title Tag: Jeff Ferris (modified by Gary B to add title)")
	adds.pause()
	print("	Chests: jgs on retrojunkie.com (open), unknown on retrojunkie.com (closed)")
	adds.pause()
	print("	Dragon: Maxi Rose")
	adds.pause()
	print("	King Dragon: unknown on chris.com")
	adds.pause()
	print("	Ghost: jgs on retrojunkie.com")
	adds.pause()
	print("	ASCII Bubble Text: Alpha and CyberMedium fonts on patorjk.com/software/taag")
	
	
	
	
	
	
	
	
	
	
	