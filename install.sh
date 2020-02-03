#!/usr/bin/env bash
# install apache, php, npm
DEBIAN_FRONTEND=noninteractive sudo apt-get update && \
    sudo apt-get install -y python3 npm apache2 php libapache2-mod-php
npm install --user localtunnel
sudo a2enmod mpm_prefork && sudo a2enmod php7.2
sudo wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip && unzip ngrok-stable-linux-amd64.zip && rm ngrok-stable-linux-amd64.zip
# Set up ngrok if needed
while true; do
  read -r -p "Is ngrok configured on this machine?{y/n} " EXISTS
  if [ "$EXISTS" == "y" ]; then
    break
  elif [ "$EXISTS" == "n" ]; then
    ./ngrok authtoken 1Wxj5KuPExFLwdtvYF0KPUgPVgb_6qXeckNfuKY2CL8Z5uxyr
    break
  fi
done


sudo service apache2 restart

printf "\n\nTo run, use command:\n\n  \033[94;1msudo python3 blackphish.py\n\n"
