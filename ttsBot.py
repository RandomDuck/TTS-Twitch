from gtts import gTTS # type: ignore
from pydub import AudioSegment
from pydub.playback import play
from twitchio.ext import commands # type: ignore
from io import BytesIO
import json;

class twitchBot(commands.Bot):
  #todo: add a raid announcment message

    def __init__(self, token, prefix, targetChannels):
        self.active = True # type: ignore
        self.prefix = prefix
        self.sayName = False
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=token, prefix=prefix, initial_channels=targetChannels)

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        print((self.nick))
        Channels = await self.join_channels([self.nick])

    def newTTS(self, text):
      # initialize tts, create mp3 and play
      mp3_fp = BytesIO()
      tts = gTTS(text, 'com')
      tts.write_to_fp(mp3_fp)
      mp3_fp.seek(0)
      play(AudioSegment.from_mp3(mp3_fp))

    @commands.command()
    async def tts(self, ctx: commands.Context): # make tts
        if (self.active):
          message = ctx.message.content[len(self.prefix)+3:]
          self.newTTS(f'{ctx.author.name} says {message}' if self.sayName else message)

    @commands.command()
    async def about(self, ctx: commands.Context): #tell us about the channel
        aboutText = "test"
        if (self.active):
          ctx.message.channel.send(aboutText)

    @commands.command()
    async def help(self, ctx: commands.Context): #list commands and their use
        helpText = "test"
        if (self.active):
          ctx.message.channel.send(helpText)

    @commands.command()
    async def shoutout(self, ctx: commands.Context): #shoutout a user
      pass

    @commands.command()
    async def rules(self, ctx: commands.Context): #display rule number x or all rules/link to rules 
      pass

    @commands.command()
    async def discord(self, ctx: commands.Context): #display the discord join link
      pass

    @commands.command()
    async def placeholder(self, ctx: commands.Context): #placeholder function to make more commands
      pass

if __name__ == "__main__":
  config = {}
  with open('config.json') as f:
    config = json.load(f)
  bot = twitchBot(config['twitchKey'], config['prefix'], config['targetChannels'])
  bot.sayName=True
  bot.run()