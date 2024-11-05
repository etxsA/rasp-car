# Utilities 
Folder used to save utilities used for the project, none of them are dependencies. 

## Ip Addr Telegram Bot
The car is connected to a network that may have dynamic ips, the tools makes the raspberry, send it's current ip addr, to a telegram, bot so you can know the ip in the current net without using any kind of physical input or output.

### Bot Setup
You need to create a bot in telegram, for this simply search the user BotFather and follow the commands to create a bot, you will be granted with a bot token. 

1. After obtaining the token start a conversation with your own bot from the device you would like to receive the ip addr. 

2. Send a get request to the getUpdates endpoit, you need to obtain the ChatId of your chat. 

```bash
https://api.telegram.org/bot<your_bot_token>/getUpdates
```

Example response:

```json
{
  "ok": true,
  "result": [
    {
      "update_id": 123456789,
      "message": {
        "message_id": 1,
        "from": {
          "id": 123456789,
          "is_bot": false,
          "first_name": "YourName",
          "last_name": "YourLastName",
          "username": "your_username",
          "language_code": "en"
        },
        "chat": {
          "id": 123456789,
          "first_name": "YourName",
          "last_name": "YourLastName",
          "username": "your_username",
          "type": "private"
        },
        "date": 1612024873,
        "text": "Hello"
      }
    }
  ]
}

```

4. Edit this varibles into the bash script
```bash
#Edit your creds
botToken ="token"
chatId ="chatId"
```

5. Finally Run the script to make a service.

```bash
chmod +x ./botIP ; chmod +x ./makeBotService.sh
sudo makeBotService.sh
```

6. Done, it should work on startup after it connects to the network.
Also the script runs once for testing, you should receive a message on the specified chat id. 