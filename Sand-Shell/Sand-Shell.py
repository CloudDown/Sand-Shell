import os
from time import sleep
import webbrowser
from termcolor import colored
import subprocess, sys
from subprocess import Popen, PIPE
import configparser
from datetime import datetime

if __name__ == '__main__':
#variable



#config code
    title_color = "yellow"
    command_color = "yellow"
    title = colored('''
                   ____                      
                  (_  _)      _____                 _        _____ _          _ _                         
        .  .       / /       /  ___|               | |      /  ___| |        | | |                        
     .`_._'_..    / /        \ `--.  __ _ _ __   __| |______\ `--.| |__   ___| | |                        
     \   o   /   / /          `--. \/ _` | '_ \ / _` |______|`--. \ '_ \ / _ \ | |                        
      \ /   /  _/ /_         /\__/ / (_| | | | | (_| |      /\__/ / | | |  __/ | |                        
 . ~. `\___/'./~.' /.~'`.    \____/ \__,_|_| |_|\__,_|      \____/|_| |_|\___|_|_|     Shell By CloudDown 
 ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
''',title_color)

#code   

    os.system( "title Sand-Shell" )
    print (title)
    print(colored("ㅤㅤㅤㅤㅤㅤㅤmode 1 : [🏖️]", 'yellow'), end="")
    print(colored("ㅤㅤㅤㅤㅤmode 2 : [🕹️]", 'red'), end="")
    print(colored("ㅤㅤㅤㅤㅤmode 3 : [⏬]", 'cyan'), end="")
    print(colored("ㅤㅤㅤㅤㅤmode 4 : [⚙️]", 'green'))
    print(" ")
    print(colored('ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤTYPE HELP FOR SHOW ALL COMMANDS', 'white', attrs=['bold']))
    os.system ("C:\Windows\Sand-Shell\shell.py")