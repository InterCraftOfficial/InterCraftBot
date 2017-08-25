from . command import *
from mcstatus import MinecraftServer


class MinecraftCommand(Command):

	def __init__(self, config):
		super(MinecraftCommand, self).__init__(config)
		self.__config = config
		self.__creativeServer = MinecraftServer.lookup(self.__config['minecraft']['address_creative'])
		self.__survivalServer = MinecraftServer.lookup(self.__config['minecraft']['address_survival'])


	def status(self, message):

		result = ""
		if message.content == 'creative':
			result = "Status of creative server:\n\n"
			server = self.__creativeServer
		else:
			result = "Status of survival server:\n\n"
			server = self.__survivalServer

		status = server.status()
		result += 'Latency: ' + str(status.latency) + 'ms\n'
		result += 'Players online: ' + str(status.players.online)

		# Because for some reason it returns `None` instead of an empty list
		if status.players.sample:
			for player in status.players.sample:
				result += '\n  ' + player.name
		return result


commandClass = MinecraftCommand
