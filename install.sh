sudo apt-get install python3
sudo apt-get install ssh
sudo apt-get install apache2
sudo npm install -g localtunnel
sudo a2enmod mpm_prefork && sudo a2enmod php7.2

# End #
service apache2 restart

printf "\n\n\To run, use command:\n\n  \033[94;1msudo python3 blackphish.py\n\n"
