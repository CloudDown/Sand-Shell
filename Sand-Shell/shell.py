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

    commandsand = input(colored(r"[🏖️] !>",'yellow')).lower()
    now = datetime.now()


    if commandsand == ("clear"):
        os.system("cls")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nClear "+(now.strftime("%D (%H:%M:%S)")))
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
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nopen log "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("clear log"):
        os.system("del C:\windows\Sand-Shell\log.txt")
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nClear log "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("author"):
        webbrowser.open('https://github.com/CloudDown')
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nAuthor "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("pwd"):
        os.system("powershell")
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nPowershell "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("cloud shell") or commandsand == ("cs"):
        webbrowser.open('https://shell.cloud.google.com/?hl=fr&fromcloudshell=true&show=terminal&pli=1')
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nCloudShell "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main() 

    if commandsand == ("instagram") or commandsand == ("insta"):
        webbrowser.open('https://www.instagram.com')
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nInstagram "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("tiktok"):
        webbrowser.open('https://www.tiktok.com')
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nTiktok "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()   
        main()
        

    if commandsand == ("twitter"):
        webbrowser.open('https://www.twitter.com')
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nTwitter "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()  

    if commandsand == ("reddit"):
        webbrowser.open('https://www.reddit.com')
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nReddit "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("youtube") or commandsand == ("ytb") or commandsand == ("yt"):
        webbrowser.open('https://www.youtube.com')
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nYoutube "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()
        
    if commandsand == ("twitch") or commandsand == ("ttv") or commandsand == ("tv)"):
        webbrowser.open('https://www.twitch.tv')
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nTwitch "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("discord") or commandsand == ("ds"):
        os.system(r"%USERPROFILE%\AppData\Local\Discord\Update.exe --processStart Discord.exe")
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nDiscordApp "+(now.strftime("%D (%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("config") or commandsand == ("DS"):
        os.system("notepad.exe C:\windows\Sand-Shell\config.ini")
        print(" ")
        fichier = open("C:\windows\Sand-Shell\log.txt", "a")
        fichier.write("\nConfig "+(now.strftime("%D (%H:%M:%S)")))
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
    title_color = "yellow"
    command_color = "yellow"
    os.system( "title Sand-Shell" )
    print(" ")
    print(colored('Default Mod Loaded ✅', 'yellow', attrs=['bold']))
    print(" ")
    main()    