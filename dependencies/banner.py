#!/usr/bin/python3
from termcolor import colored

def banner():
	banner = """_________               __________.__    .__       .__     
\\_   ___ \\_____    _____\\______   \\  |__ |__| _____|  |__  
/    \\  \\/\\__  \\  /     \\|     ___/  |  \\|  |/  ___/  |  \\ 
\\     \\____/ __ \\|  Y Y  \\    |   |   Y  \\  |\\___ \\|   Y  \\
 \\______  (____  /__|_|  /____|   |___|  /__/____  >___|  /
        \\/     \\/      \\/              \\/        \\/     \\/ 
			Say Cheese :)
	"""

	return colored(banner, 'green')

