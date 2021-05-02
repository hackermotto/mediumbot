#!/bin/bash

sudo apt install git -y
sudo apt install jq -y
sudo apt install firefox -y
sudo apt install chromium -y

git clone https://github.com/hackermotto/WebDriversManager

cd WebDriversManager
chmod +x ./wdm.sh
./wdm.sh install gecko
./wdm.sh install chrome


cp mediumbot.service /etc/systemctl/system/mediumbot.service

sudo systemctl daemon-reload
sudo systemctl enable mediumbot.service
sudo systemctl start mediumbot.service