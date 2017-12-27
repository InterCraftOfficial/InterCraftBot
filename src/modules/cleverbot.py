from cleverwrap import CleverWrap


class Cleverbot:

	def __init__(self, apiKey):
		self.__apiKey = apiKey
		self.__sessions = {}


	def send(self, author, message):
		if author not in self.__sessions:
			print("Adding new author")
			self.__sessions[author] = CleverWrap(self.__apiKey)
		try:
			return self.__sessions[author].say(message)
		except Exception as e:
			print(e)
			return None
