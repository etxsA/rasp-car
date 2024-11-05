#!/bin/bash

sudo cp ./botIp.sh /home/$USER/botIp.sh
sudo chmod +x /home/$USER/botIp.sh
sudo cp ./telegramBot.service /etc/systemd/system/telegramBot.service
sudo systemctl daemon-reload
sudo systemctl enable telegramBot.service
sudo systemctl status telegramBot.service
