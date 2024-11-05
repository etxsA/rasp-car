#!/bin/bash

sudo cp ./botIp.sh /usr/local/bin/botIp.sh
sudo chmod +x /usr/local/bin/botIp.sh
sudo cp ./telegramBot.service /etc/systemd/system/telegramBot.service
sudo chown root:root /etc/systemd/system/telegramBot.service
sudo chmod 644 /etc/systemd/system/telegramBot.service
sudo systemctl daemon-reload
sudo systemctl enable telegramBot.service
sudo systemctl start telegramBot.service
sudo systemctl status telegramBot.service

