from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout # type: ignore
from threading import Thread


class gui(QWidget):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

        self.setWindowTitle("TTS-Control")
        self.text="Listening" if self.bot.active else "Muted"
        self.textName="say names" if self.bot.sayName else "not say names"
        self.button = QPushButton(f"TTS IS: {self.text}")
        self.buttonName = QPushButton(f"Bot will: {self.textName}")
        self.button.pressed.connect(self.toggleBot)
        self.buttonName.pressed.connect(self.toggleNames)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(self.button)
        layout.addWidget(self.buttonName)

        self.show()

    def toggleBot(self, *args):
        self.bot.active = not self.bot.active
        self.text="Listening" if self.bot.active else "Muted"
        self.button.setText(f"TTS IS: {self.text}")

    def toggleNames(self, *args):
        self.bot.sayName = not self.bot.sayName
        self.textName="say names" if self.bot.sayName else "not say names"
        self.buttonName.setText(f"Bot will: {self.textName}")

