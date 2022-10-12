import os
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')
title_color = config.get('COLOR','Title')
title = ('\033[1;33m'r'''
                   ____                      
                  (_  _)      _____                 _        _____ _          _ _                         
        .  .       / /       /  ___|               | |      /  ___| |        | | |                        
     .`_._'_..    / /        \ `--.  __ _ _ __   __| |______\ `--.| |__   ___| | |                        
     \   o   /   / /          `--. \/ _` | '_ \ / _` |______|`--. \ '_ \ / _ \ | |                        
      \ /   /  _/ /_         /\__/ / (_| | | | | (_| |      /\__/ / | | |  __/ | |                        
 . ~. `\___/'./~.' /.~'`.    \____/ \__,_|_| |_|\__,_|      \____/|_| |_|\___|_|_|     Shell By CloudDown 
 ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
''')

#code   

os.system( "title Sand-Shell" )
print (title)
print("", end="")
print('\033[1;33m',"ㅤㅤㅤㅤㅤㅤㅤmode 1 : [🏖️]", end="")
print("", end="")
print('\033[1;31m',"ㅤㅤㅤㅤㅤmode 2 : [🕹️]", end="")
print("", end="")
print('\033[1;36m',"ㅤㅤㅤㅤㅤmode 3 : [⏬]", end="")
print("", end="")
print('\033[1;32m',"ㅤㅤㅤㅤㅤmode 4 : [⚙️]")
print("\033[0m")
print('\033[3m''ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤTYPE HELP FOR SHOW ALL COMMANDS')
os.system ("C:\Windows\Sand-Shell\shell.py")