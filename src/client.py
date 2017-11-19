import discord
import asyncio

from commands.command_manager import *


class InterCraftBot(discord.Client):

    def __init__(self):
        super(InterCraftBot, self).__init__()
        self.__commandManager = CommandManager()


    @asyncio.coroutine
    def on_ready(self):
        print('Logged in as:')
        print(self.user.name)
        print(self.user.id)


    @asyncio.coroutine
    def on_message(self, message):

        if message.content.startswith('!'):
            result = self.__commandManager.execute(message)
            if (result is not None):
                yield from self.send_message(message.channel, result)

    @asyncio.coroutine
    def on_member_join(self, member):
        yield from self.send_message(member, "Welcome to the InterCraft Discord server! In order for you to join the server, you will need an admin to approve you. But feel free to chat in the InterCraft lounge, both on voice and in chat!")
        yield from self.send_message(member, "An admin is usually on later in the day CST, so try checking back then!")
