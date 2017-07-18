from . command import *
from mcstatus import MinecraftServer


class MinecraftCommand(Command):

	def __init__(self):
		self.__survivalServer = MinecraftServer.lookup("survival.intercraftmc.com")
		self.__creativeServer = MinecraftServer.lookup("creative.intercraftmc.com")


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
		return result


commandClass = MinecraftCommand