#!/usr/local/bin/python3
import json
from threading import Thread
from PyQt6.QtWidgets import QApplication # type: ignore
from ttsBot import twitchBot
from ttsUI import gui
import sys

config = {}
with open('config.json') as f:
    config = json.load(f)

bot = twitchBot(config['twitchKey'], config['prefix'], config['targetChannels'])
app = QApplication(sys.argv)
ui = gui(bot)

def runBot():
    bot.run()

def runUI():
    app.exec()



if __name__ == "__main__":
    botT = Thread(target=runBot)
    botT.start()
    runUI()
