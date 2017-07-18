from . command import *
from mcstatus import MinecraftServer


class MinecraftCommand(Command):

	def __init__(self):
		self.__server = MinecraftServer.lookup("survival.intercraftmc.com")


	def status(self, message):
		status = self.__server.status()
		result = 'Latency: ' + str(status.latency) + 'ms\n'
		result += 'Players online: ' + str(status.players.online)
		return result


commandClass = MinecraftCommand