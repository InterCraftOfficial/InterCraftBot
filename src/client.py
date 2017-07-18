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

        # if message.content.lower().startswith('!touch'):
        #     yield from self.send_message(message.channel, "Don't touch me you pervert!")

        # if message.content.lower().startswith('!put into'):
        #     messageCommand = message.content.split()

        #     if messageCommand[2] == 'soup':
        #         global soup
        #         soup.addIngredient(messageCommand[3])
        #         if soup.checkIngredient(messageCommand[3]) == 1:
        #             theText = "Added a " + str(messageCommand[3]) + " to the soup. There is " + str(soup.checkIngredient(messageCommand[3])) + " " + str(messageCommand[3]) + " in the soup."
        #         else:
        #             theText = "Added a " + str(messageCommand[3]) + " to the soup. There are " + str(soup.checkIngredient(messageCommand[3])) + " " + str(messageCommand[3]) + "s in the soup."

        #         yield from self.send_message(message.channel, theText)

        # if message.content.lower().startswith('!soup'):
        #     messageCommand = message.content.split()
        #     global soup
        #     if messageCommand[1] == 'status':
        #         soupKeys = soup.getStatus()
        #         theText = ""
        #         for ingredients in soupKeys:
        #             if soup.checkIngredient(ingredients) == 1:
        #                 theText += "There is " + str(soup.checkIngredient(ingredients)) + " " + str(ingredients) + " in the soup \n"
        #             else:
        #                 theText += "There are " + str(soup.checkIngredient(ingredients)) + " " + str(ingredients) + "s in the soup \n"

        #         yield from self.send_message(message.channel, theText)

    @asyncio.coroutine
    def on_member_join(self, member):
        yield from self.send_message(member, "Welcome to the InterCraft Discord server! In order for you to join the server, you will need an admin to approve you. But feel free to chat in the InterCraft lounge, both on voice and in chat!")
        yield from self.send_message(member, "An admin is usually on later in the day CST, so try checking back then!")
