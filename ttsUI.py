from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout # type: ignore
from threading import Thread


class gui(QWidget):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

        self.setWindowTitle("TTS-Control")
        self.text="Listening" if self.bot.active else "Inactive"
        self.textTts="Speaking" if self.bot.commandActive('tts') else "Muted"
        self.textName="say names" if self.bot.sayName else "not say names"
        self.button = QPushButton(f"Bot IS: {self.text}")
        self.buttonTts = QPushButton(f"TTS IS: {self.textTts}")
        self.buttonName = QPushButton(f"Bot will: {self.textName}")
        self.button.pressed.connect(self.toggleBot)
        self.buttonTts.pressed.connect(self.toggleTts)
        self.buttonName.pressed.connect(self.toggleNames)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(self.button)
        layout.addWidget(self.buttonTts)
        layout.addWidget(self.buttonName)

        self.show()

    def toggleBot(self, *args):
        self.bot.active = not self.bot.active
        self.text="Listening" if self.bot.active else "Inactive"
        self.button.setText(f"Bot IS: {self.text}")

    def toggleTts(self, *args):
        self.bot.settings['activeCommands']['tts'] = not self.bot.commandActive('tts')
        self.textTts="Speaking" if self.bot.commandActive('tts') else "Muted"
        self.buttonTts.setText(f"TTS IS: {self.textTts}")

    def toggleNames(self, *args):
        self.bot.sayName = not self.bot.sayName
        self.textName="say names" if self.bot.sayName else "not say names"
        self.buttonName.setText(f"Bot will: {self.textName}")

