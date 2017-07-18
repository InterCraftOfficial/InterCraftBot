import inflect
import random
import re

from . command import *
from modules.soup import *

class SoupCommand(Command):

	def __init__(self):
		self.__inflect = inflect.engine()
		self.__soup = Soup()

	def add(self, message):
		if not message.content:
			return "Ok, adding nothing to the soup"

		ingredients = re.split('\,\s*', message.content)

		for ingredient in ingredients:
			parts = re.split('[\s]+', ingredient.strip())
			quantity = 1
			print(parts)
			if len(parts) > 1 and parts[0].isdigit():
				print('It\'s a digit')
				quantity = int(parts[0])
				del parts[0]
			self.__soup.addIngredient(' '.join(parts), quantity)

		responses = [
			'Mmmmm delicious',
			'Sounds great',
			'Sure thing',
			'That is exactly what this soup needs'
		]

		return responses[random.randint(0, len(responses) - 1)]


	def recipe(self, message):
		ingredients = self.__soup.ingredients()
		result = 'The soup contains the following:'
		for ingredient in ingredients:
			quantity = self.__soup.ingredientCount(ingredient)
			result += '\n' + str(quantity) + ' ' + self.__inflect.plural(ingredient, quantity)

		return result.strip('\n')


commandClass = SoupCommand