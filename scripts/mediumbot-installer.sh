#!/usr/bash

sudo apt install firefox
sudo apt install chromium

git clone https://github.com/hackermotto/WebDriversManager

cd WebDriversManager
chmod +x ./wdm.sh
./wdm.sh install gecko
./wdm.sh install chrome

cp mediumbot.service /etc/systemctl/system/mediumbot.service

sudo systemctl enable mediumbot.service
sudo systemctl start mediumbot.service