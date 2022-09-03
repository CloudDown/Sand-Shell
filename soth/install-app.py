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

    commandsand = input(colored(r"[⏬] !> ",'cyan')).lower()
    now = datetime.now()


    if commandsand == ("clear"):
        os.system("cls")
        fichier = open("C:\windows\soth\log.txt", "a")
        fichier.write("\nClear "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("help"):
        os.system("help.html")
        print(" ")
        fichier = open("C:\windows\soth\log.txt", "a")
        fichier.write("\nHelp "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("log"):
        os.system("type C:\windows\soth\log.txt")
        print(" ")
        main()

    if commandsand == ("author"):
        webbrowser.open('https://github.com/CloudDown')
        print(" ")
        fichier = open("C:\windows\soth\log.txt", "a")
        fichier.write("\nAuthor "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main()


    if commandsand == ("discord"):
        webbrowser.open('https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86')
        os.system ("pause")
        os.system (r"%USERPROFILES%\Downloads\DiscordSetup.exe")
        print(" ")
        fichier = open("C:\windows\soth\log.txt", "a")
        fichier.write("\nInstall Discord "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("spotify"):
        os.system ("spot-install.bat")
        os.system ("pause")
        print(" ")
        fichier = open("C:\windows\soth\log.txt", "a")
        fichier.write("\nInstall Spotify "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("mod 1"):
        os.system ("C:\windows\soth\shell.py")
        print(" ")
        fichier = open("C:\windows\soth\log.txt", "a")
        fichier.write("\nmod 1 "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("mod 2"):
        os.system ("C:\windows\soth\game.py")
        print(" ")
        fichier = open("C:\windows\soth\log.txt", "a")
        fichier.write("\nmod 2 "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("mod 3"):
        os.system ("C:\windows\soth\install-app.py")
        print(" ")
        fichier = open("C:\windows\soth\log.txt", "a")
        fichier.write("\nmod 3 "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("mod 4"):
        os.system ("C:\windows\soth\settings.py")
        print(" ")
        fichier = open("C:\windows\soth\log.txt", "a")
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
    print(colored('Install App Mod Loaded ✅', 'cyan', attrs=['bold']))
    print(" ")
    main()    