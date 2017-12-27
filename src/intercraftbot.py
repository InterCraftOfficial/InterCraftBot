import discord
import asyncio

from commands.command_manager import *
from modules.cleverbot import *
from utils.config import *


class InterCraftBot(discord.Client):

    def __init__(self):
        super(InterCraftBot, self).__init__()
        self.__config = Config()
        self.__commandManager = CommandManager(self.__config)
        self.__cleverbot = None
        self.__modmail = None


    # Override the default run method to extend functionality
    def run(self):
        if not self.__config.load():
            return 1
        
        self.__cleverbot = Cleverbot(self.__config['cleverbot']['key'])

        return super(InterCraftBot, self).run(self.__config['discord']['key'])


    @asyncio.coroutine
    def on_ready(self):
        print('Logged in as:')
        print(self.user.name)
        print(self.user.id)
        if len(self.servers) != 1 or self.__config["discord"]["modmail"] == "":
            print("Modmail disabled.")
        else:
            self.__modmail = discord.utils.get(self.get_all_channels(),
                                               name=self.__config["discord"]["modmail"])


    @asyncio.coroutine
    def on_message(self, message):

        if message.content.startswith('!'):
            result = self.__commandManager.execute(message)
            if (result is not None):
                yield from self.send_message(message.channel, result)

        elif len(message.mentions):
            isMentioned = False
            for mention in message.mentions:
                message.content = message.content.replace(mention.mention, "")
                if mention.id == self.user.id:
                    isMentioned = True
            if isMentioned:
                yield from self.send_message(message.channel, self.__cleverbot.send(message.author, message.content))

        elif message.channel.is_private and message.author != self.user and self.__modmail != None:
            yield from self.send_message(self.__modmail, "**{}**: {}".format(message.author.name, message.content))
            yield from self.send_message(message.channel, "Thank you! I've forwarded your request to the mods!")

    @asyncio.coroutine
    def on_member_join(self, member):
        yield from self.send_message(member, "Welcome to the InterCraft Discord server! In order for you to join the server, you will need an admin to approve you. But feel free to chat in the InterCraft lounge, both on voice and in chat!")
        yield from self.send_message(member, "An admin is usually on later in the day CST, so try checking back then!")

        if self.__modmail != None:
            yield from self.send_message(self.__modmail, "A new user joined: {}".format(member.name))
