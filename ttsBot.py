from gtts import gTTS # type: ignore
from pydub import AudioSegment # type: ignore
from pydub.playback import play # type: ignore
from twitchio.ext import commands # type: ignore
from io import BytesIO
import json;

class twitchBot(commands.Bot):
  #todo: add a raid announcment message

    def __init__(self, token, prefix, targetChannels):
        self.settings = {}
        with open('settings.json') as f:
            self.settings = json.load(f)
        self.active = True # type: ignore
        self.ttsActive = True # type: ignore
        self.prefix = prefix
        self.sayName = True
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=token, prefix=prefix, initial_channels=targetChannels, case_insensitive=True)

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
    
    def commandActive(self, command):
      return self.settings['activeCommands'][command]
    
    def getMessage(self, command):
      return self.settings['messages'][command]
    

    async def event_raided(self, channel, user, raid_count): #detect raid
        print(f'Raid detected! {user} raided {channel} with {raid_count} viewers!')
        if (self.active and self.commandActive('raid')):
          await channel.send(self.getMessage('raid').format(n=raid_count, u=user))

    @commands.command()
    async def tts(self, ctx: commands.Context): #make tts
        if (self.active and self.commandActive('tts')):
          message = ctx.message.content[len(self.prefix)+3:]
          self.newTTS(f'{ctx.author.name} says {message}' if self.sayName else message)

    @commands.command()
    async def about(self, ctx: commands.Context): #tell us about the channel
        if (self.active and self.commandActive('about')):
          await ctx.message.channel.send(self.getMessage('about'))

    @commands.command()
    async def help(self, ctx: commands.Context): #list commands and their use
        if (self.active and self.commandActive('help')):
          await ctx.message.channel.send(self.getMessage('help'))

    @commands.command()
    async def shoutout(self, ctx: commands.Context): #shoutout a user
      if (self.active and self.commandActive('shoutout')):
        message = ctx.message.content[len(self.prefix)+8:]
        await ctx.message.channel.send(self.getMessage('shoutout').format(u=message))

    @commands.command()
    async def rules(self, ctx: commands.Context): #display rule number x or all rules/link to rules 
        if (self.active and self.commandActive('rules')):
          await ctx.message.channel.send(self.getMessage('rules'))

    @commands.command()
    async def discord(self, ctx: commands.Context): #display the discord message
        if (self.active and self.commandActive('discord')):
          await ctx.message.channel.send(self.getMessage('discord'))

    @commands.command()
    async def soundboard(self, ctx: commands.Context): #soundboard plays sounds on stream
      if (self.active and self.commandActive('soundboard')):
        pass
      pass

    @commands.command()
    async def placeholder(self, ctx: commands.Context): #placeholder function to make more commands
      if (self.active and self.commandActive('placeholder')):
        pass
      pass

if __name__ == "__main__":
  config = {}
  with open('config.json') as f:
    config = json.load(f)
  bot = twitchBot(config['twitchKey'], config['prefix'], config['targetChannels'])
  bot.run()
