#!/bin/bash

cp ./botIp.sh /home/${whoami}/botIp.sh
chmod +x /home/${whoami}/botIp.sh
cp ./telegramBot.service /etc/systemd/system/telegramBot.service
systemctl daemon-reload
systemctl enable telegramBot.service
systemctl status telegramBot.service
