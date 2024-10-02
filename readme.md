# TTS bot for twitch
This is a tts bot for twitch you can run local on your own machine. it requires FFMPEG to work.

### To install 
Simply make sure FFMPEG and python is installed then run
>pip install -r requirmenets.txt

after that make sure to edit the `config.json` with a bot access token,\
if ur using ur own twitch account as the bot you dont need to do anything else, The bot will automatically join your twitch chat\
however if ur using an actuall bot account you must also specify the channels you want it to join in the `config.json`

config Example
```json
 {
    "twitchKey": "TOKEN12312331",
    "prefix": "!",
    "targetChannels": ['dougdoug'] // will join the doug doug twitch chat
  }
```


To ensure you have the right channel for ur purpose you can simply look att the URL of the twitch streamer page (ex. [twitch.tv/dougdoug](https://www.twitch.tv/dougdoug))

### Running the bot
you can choose to run it with or without the control panel.\
To run with control panel:
>python main.py

To run without control panel:
>python ttsBot.py
