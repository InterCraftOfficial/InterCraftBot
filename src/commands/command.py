import inspect
import re

class Command:

	def __init__(self, config):

		# Make the config pretty hidden
		self.__config__ = config 


	def commandMethod(self, name):
		if name == 'exec_':
			return None

		methods = inspect.getmembers(self, predicate=inspect.ismethod)
		for method in methods:
			if method[0] == name:
				return method[1]
		return None


	def exec_(self, message):
		parts = re.split('([\s]+)', message.content)
		print("Executing...", parts)
		if len(parts) > 0 and len(parts[0]) > 0:
			method = self.commandMethod(parts[0])
			if method:
				if len(parts) > 1 and len(parts[2]) > 0:
					arguments = ''.join(parts[2:]) # Strip the command part out of the command line
				else:
					arguments = None
			else:
				method = self.commandMethod('run')
				arguments = ''.join(parts)
		else:
			method = self.commandMethod('run')
			arguments = None

		if method:
			message.content = arguments
			return method(message)