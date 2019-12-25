#!/usr/bin/bash

sudo apt-get install python3
sudo apt-get install ssh
sudo apt-get install apache2
sudo npm install -g localtunnel
sudo apt-get install php libapache2-mod-php
sudo a2enmod mpm_prefork && sudo a2enmod php7.2

# End #
service apache2 restart

printf "\n\n\033[92;1msudo python3 blackphish.py\033[0m to run\n\n"