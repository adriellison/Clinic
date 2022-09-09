from colorconsole import terminal

from .simple import *

screen = terminal.get_terminal(conEmu=False)

def logo():
	cls()
	carregar()
	screen.cprint(6, 0,'''

	 	 _____  _       _                           
		/  ___|(_)     | |                          
		\ `--.  _  ___ | |_   ___  _ __ ___    __ _ 
	 	 `--. \| |/ __|| __| / _ \| '_ ` _ \  / _` |
		/\__/ /| |\__ \| |_ |  __/| | | | | || (_| |
		\____/ |_||___/ \__| \___||_| |_| |_| \__,_|

			 _____  _  _         _       
			/  __ \| |(_)       (_)      
			| /  \/| | _  _ __   _   ___ 
			| |    | || || '_ \ | | / __|
			| \__/\| || || | | || || (__ 
			 \____/|_||_||_| |_||_| \___|

			       Version Alpha 3.5
	''')
	screen.reset_colors()
	espaco()
	input('\t\t\t    Pressione para continuar')
	cls()