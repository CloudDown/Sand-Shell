import os
from time import sleep
import webbrowser
from termcolor import colored
import subprocess, sys
from subprocess import Popen, PIPE
import configparser
from datetime import datetime


def main():
#variable

    commandsand = input(colored(r"[⚙️] !> ",'green')).lower()
    now = datetime.now()


    if commandsand == ("clear"):
        os.system("cls")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nClear "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("help"):
        os.system("C:\windows\Sand-Shell\help.html")
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nHelp "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("log"):
        os.system("type C:\windows\Sand-Shell\log.txt")
        print(" ")
        main()

    if commandsand == ("config") or commandsand == ("DS"):
        os.system("notepad.exe C:\windows\Sand-Shell\config.ini")
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nConfig "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("author"):
        webbrowser.open('https://github.com/CloudDown')
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nAuthor "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("mod 1"):
        os.system ("C:\windows\Sand-Shell\shell.py")
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nmod 1 "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("mod 2"):
        os.system ("C:\windows\Sand-Shell\game.py")
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nmod 2 "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("mod 3"):
        os.system ("C:\windows\Sand-Shell\install-app.py")
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nmod 3 "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("mod 4"):
        os.system ("C:\windows\Sand-Shell\settings.py")
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nmod 4 "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()
  
    
    if commandsand == (""):
        print(" ")
        main()
    else:
        print(" ")
        os.system(commandsand)
        print(" ")
        main()


if __name__ == '__main__':
#variable


#code   

    os.system( "title Sand-Shell" )
    print(" ")
    print(colored('Settings Mod Loaded ✅', 'green', attrs=['bold']))
    print(" ")
    main()    