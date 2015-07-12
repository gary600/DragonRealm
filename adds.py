import os
import sys
import time
#Getch() Import
# Getch for Linux, processes the key inputs
# by louis on StackOverflow

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
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
def pause():
	time.sleep(0.1)
def longpause():
	time.sleep(2)