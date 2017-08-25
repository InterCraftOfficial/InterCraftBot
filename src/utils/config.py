import json

class Config():

	def __init__(self):
		self.__config = {}


	def load(self):
		"""Load the configuration, return the result as a boolean"""
		try:
			f = open("./config.json")
			self.__config = json.load(f)
			f.close()
		except OSError as e:
			print("Unable to find config.json", e)
			return False
		except json.JSONDecodeError as e:
			print("Failed to decode config.json", e)
			return False
		return True


	def __getitem__(self, category):
		"""Return the requested category from the configuration"""
		return self.__config[category]
