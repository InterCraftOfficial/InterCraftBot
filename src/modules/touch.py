

class Touch():

	def __init__(self):
		self.__touches = {}


	def touch(self, member):
		if member in self.__touches:
			self.__touches[member] += 1
		else:
			self.__touches[member] = 1


	def touchCount(self, member):
		if member in self.__touches:
			return self.__touches[member]
		return 0


	def reset(self, member):
		if member in self.__touches:
			del self.__touches[member]
			