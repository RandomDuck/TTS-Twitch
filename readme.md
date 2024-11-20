# TTS bot for twitch
This is a tts bot for twitch you can run local on your own machine. it requires FFMPEG to work.

# To install 
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

# Running the bot
you can choose to run it with or without the control panel.\
To run with control panel:
>python main.py

To run without control panel:
>python ttsBot.py


### dealing with settings
The settings file has values to personalise ur bot experiance.
#### disabling commands
Commands can be disabled on the go in the UI, However to Disable the commands on boot (or to change the default state of a command) you must edit the config by changing them from "true" to "false", this requires.
```json
"activeCommands": { 
    "tts": true,
    "about": true,
    "help": true,
    "shoutout": true,
    "rules": true,
    "discord": true,
    "soundboard": true
  },
```
#### custom messages
in messages some commands (Currently shoutout and Raid) have some runtime variables.
use {u} for placement of the name of the user, and {n} for numerical runtime value (right no, # of raid participants).
```json
 "messages": {
    "help": "Availalbe commands include: tts: send a tts, about: info about the channel, help: list commands and their use, shoutout: shoutout a user, rules: display the rules, discord: display the discord message, soundboard: plays sounds on stream",
    "about": "Hello, welcome to my stream. I stream things for reasons. lets all have a good time.",
    "shoutout": "Hey {u}, thanks you're awesome. But not as awesome as ducks.",
    "rules": "#1 No foxes, #2 No discrimination (unless its against foxes), #3 UwU, Ara ara",
    "discord": "link to discord here: https://FAKELINK.DISCORD/Join",
    "raid": "Thank you {u} for raiding with {n} people" 
  }
```
