import inspect
import re

class Command:

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
			commandName = parts[0]
			if len(parts) > 1 and len(parts[2]) > 0:
				arguments = ''.join(parts[2:]) # Strip the command part out of the command line
			else:
				arguments = None
		else:
			commandName = 'run'
			arguments = None

		print(commandName)

		method = self.commandMethod(commandName)
		if method:
			message.content = arguments
			return method(message)