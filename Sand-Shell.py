import os
from time import sleep
import webbrowser
from termcolor import colored
import subprocess, sys
from subprocess import Popen, PIPE
import configparser
from datetime import datetime
from pynput.keyboard import Key, Controller


def main():
#variable

    keyboard = Controller
    commandsand = input(colored(r"[🏖️] !>",'yellow')).lower()
    now = datetime.now()
    ist_list = ["spotify, discord "]


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

    if commandsand == ("pwd"):
        os.system("powershell")
        print(" ")
        fichier = open("log.txt", "a")
        fichier.write("\nPowershell "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("cloud shell") or commandsand == ("cs"):
        webbrowser.open('https://shell.cloud.google.com/?hl=fr&fromcloudshell=true&show=terminal&pli=1')
        print(" ")
        fichier = open("log.txt", "a")
        fichier.write("\nCloudShell "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main() 

    if commandsand == ("instagram") or commandsand == ("insta"):
        webbrowser.open('https://www.instagram.com')
        print(" ")
        fichier = open("log.txt", "a")
        fichier.write("\nInstagram "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("tiktok"):
        webbrowser.open('https://www.tiktok.com')
        print(" ")
        fichier = open("log.txt", "a")
        fichier.write("\nTiktok "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()   
        main()
        
    if commandsand == ("auto") or commandsand == ("AUTOCLICK"):
        os.system('autoclick.exe')
        print(" ")  
        fichier = open("log.txt", "a")
        fichier.write("\nAutoclick "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()      
        main()

    if commandsand == ("twitter"):
        webbrowser.open('https://www.twitter.com')
        print(" ")
        fichier = open("log.txt", "a")
        fichier.write("\nTwitter "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main()  

    if commandsand == ("reddit"):
        webbrowser.open('https://www.reddit.com')
        print(" ")
        fichier = open("log.txt", "a")
        fichier.write("\nReddit "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("youtube") or commandsand == ("ytb") or commandsand == ("yt"):
        webbrowser.open('https://www.youtube.com')
        print(" ")
        fichier = open("log.txt", "a")
        fichier.write("\nYoutube "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main()
        
    if commandsand == ("twitch") or commandsand == ("ttv") or commandsand == ("tv)"):
        webbrowser.open('https://www.twitch.tv')
        print(" ")
        fichier = open("log.txt", "a")
        fichier.write("\nTwitch "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("discord") or commandsand == ("ds"):
        os.system(r"%USERPROFILE%\AppData\Local\Discord\Update.exe --processStart Discord.exe")
        print(" ")
        fichier = open("log.txt", "a")
        fichier.write("\nDiscordApp "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main()

    if commandsand == ("config") or commandsand == ("DS"):
        os.system("notepad.exe config.ini")
        print(" ")
        fichier = open("log.txt", "a")
        fichier.write("\nConfig "+(now.strftime("%D(%H:%M:%S)")))
        fichier.close()
        main()
    
    if commandsand == ("title color"):
        input((title_color))
        print(" ")
        main()    
#INSTALL MOD

    if commandsand == ("install discord"):
        webbrowser.open('https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86')
        sleep(2)
        keyboard.press(Key.enter)
        sleep(5)
        os.system (r"%USERPROFILES%\Downloads\DiscordSetup.exe")
        print(" ")
        fichier = open("log.txt", "a")
        fichier.write("\nInstall Discord "+(now.strftime("%D(%H:%M:%S)")))
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
    print(colored('ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤWRITE HELP FOR SHOW ALL COMMANDS', 'white', attrs=['bold']))
    print(" ")
    main()    