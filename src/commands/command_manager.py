import importlib
import re


class CommandManager:

	def __init__(self):
		
		self.__modules = {}


	def autoloadCommand(self, commandName):
		if commandName not in self.__modules:
			try:
				moduleName = commandName + '_command'
				command = getattr(importlib.__import__('commands.' + moduleName), moduleName).commandClass
				self.__modules[commandName] = command()
				print("Autoload successful for: " + commandName)
				return self.__modules[commandName]
			except ImportError:
				print("Failed to autoload command")
				return None
		else:
			return self.__modules[commandName]


	def execute(self, message):

		parts = re.split('([\s]+)', message.content)
		commandName = parts[0][1:] # Strip the '!' from the command
		command = self.autoloadCommand(commandName)
		if command:
			message.content = ''.join(parts[2:])
			return command.exec_(message)
		return None
