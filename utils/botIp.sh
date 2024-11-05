#!/bin/bash

#Edit your creds
botToken="token"
chatId="chatId"

# Get the Raspberry Pi's local IP address
ipAddr=$(hostname -I | awk '{print $1}')

# Compose the message
message="Your Raspberry Pi IP address is: $ipAddr"

# Send the message via Telegram API using curl
curl -s -X POST "https://api.telegram.org/bot$botToken/sendMessage" \
     -d chat_id="$chatId" \
     -d text="$message"


echo "Sent IP address $ipAddr to Telegram from user $USER" >> /home/$USER/ip_address_log.txt
