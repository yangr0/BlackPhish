#!/usr/bin/env bash
# install apache, php, npm
DEBIAN_FRONTEND=noninteractive sudo apt-get update && \
    sudo apt-get install -y python3 npm apache2 php libapache2-mod-php
npm install --user localtunnel
sudo a2enmod mpm_prefork && sudo a2enmod php7.2

sudo service apache2 restart

printf "\n\nTo run, use command:\n\n  \033[94;1msudo python3 blackphish.py\n\n"
