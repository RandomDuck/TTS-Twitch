from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout # type: ignore
import json


class gui(QWidget):
    def __init__(self, bot):
        super().__init__()
        # setup some default variables
        self.bot = bot
        self.commands = {}
        self.setWindowTitle("TTS-Control")
        # setup our layout box
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        # setup our widgets and display them
        self.setupDefaultWidgets()
        self.attachWidgets()
        self.show()

    def setupDefaultWidgets(self): #generate default widgets
        self.functionHeaderLabel = QLabel('Bot Control') # first label
        
        # bot control buttons 
        text="Listening" if self.bot.active else "Inactive"
        textName="say names" if self.bot.sayName else "not say names"
        self.button = QPushButton(f"Bot is: {text}")
        self.buttonName = QPushButton(f"Bot will: {textName}")
        self.button.pressed.connect(self.toggleBot)
        self.buttonName.pressed.connect(self.toggleNames)
        
        self.commandHeaderLabel = QLabel('Command Control') # second label

    def attachWidgets(self):
        # display order is set in order of apperance
        ## add our standard buttons
        self.layout.addWidget(self.functionHeaderLabel)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.buttonName)
        ## generate commands
        self.layout.addWidget(self.commandHeaderLabel)
        self.generateCommandToggles()

    def generateCommandToggles(self): # generates each command as a toggleable button
        for i in self.bot.settings['activeCommands'].keys():
            text = "Active" if self.bot.commandActive(i) else "Inactive"
            self.commands[i] = QPushButton(f"{i} is: {text}")
            self.commands[i].pressed.connect(lambda i=i: self.toggleCommand(i))
            self.layout.addWidget(self.commands[i])
        
    def toggleCommand(self, command): # handles each command toggleing on and off
        self.bot.settings['activeCommands'][command] = not self.bot.commandActive(command)
        text="Active" if self.bot.commandActive(command) else "Inactive"
        self.commands[command].setText(f"{command} is: {text}")

    ### Specific buttons with extra functionality, gets their own function ###
    def toggleBot(self):
        self.bot.active = not self.bot.active
        text="Listening" if self.bot.active else "Inactive"
        self.button.setText(f"Bot IS: {text}")

    def toggleNames(self):
        self.bot.sayName = not self.bot.sayName
        text="say names" if self.bot.sayName else "not say names"
        self.buttonName.setText(f"Bot will: {text}")

