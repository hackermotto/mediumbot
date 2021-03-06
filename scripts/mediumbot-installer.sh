#!/bin/bash

sudo apt update -y
sudo apt upgrade -y
sudo apt install git -y
sudo apt install jq -y
sudo apt install firefox -y
sudo apt install chrome-browser -y
sudo apt-get install xvfb -y

git clone https://github.com/hackermotto/WebDriversManager

cd WebDriversManager
chmod +x ./wdm.sh
./wdm.sh install gecko
./wdm.sh install chrome


sudo apt-get install lubuntu-desktop -y
sudo apt-get install tightvncserver -y
vncserver

# cp mediumbot.service /etc/systemctl/system/mediumbot.service

# sudo systemctl daemon-reload
# sudo systemctl enable mediumbot.service
# sudo systemctl start mediumbot.service