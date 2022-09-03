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
        fichier = open("log.txt", "a")
        fichier.write("\nClear "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("help"):
        os.system("help.html")
        print(" ")
        fichier = open("log.txt", "a")
        fichier.write("\nHelp "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("log"):
        os.system("type log.txt")
        print(" ")
        main()

    if commandsand == ("author"):
        webbrowser.open('https://github.com/CloudDown')
        print(" ")
        fichier = open("log.txt", "a")
        fichier.write("\nAuthor "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("mod 1"):
        os.system ("D:\GithubFiles\Projets\Sand-Shell\soth\shell.py")
        print(" ")
        fichier = open("log.txt", "a")
        fichier.write("\nmod 1 "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("mod 2"):
        os.system ("D:\GithubFiles\Projets\Sand-Shell\soth\game.py")
        print(" ")
        fichier = open("log.txt", "a")
        fichier.write("\nmod 2 "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("mod 3"):
        os.system ("D:\GithubFiles\Projets\Sand-Shell\soth\install-app.py")
        print(" ")
        fichier = open("log.txt", "a")
        fichier.write("\nmod 3 "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("mod 4"):
        os.system ("D:\GithubFiles\Projets\Sand-Shell\soth\settings.py")
        print(" ")
        fichier = open("log.txt", "a")
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