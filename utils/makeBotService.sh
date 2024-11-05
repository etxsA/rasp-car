#!/bin/bash

sudo cp ./botIp.sh /usr/local/bin/botIp.sh
sudo chmod +x /usr/local/bin/botIp.sh
sudo cp ./telegramBot.service /etc/systemd/system/telegramBot.service
sudo systemctl daemon-reload
sudo systemctl enable telegramBot.service
sudo systemctl status telegramBot.service
