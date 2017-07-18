from . command import *
from modules.math_string_parser import *


class CalcCommand(Command):

	def __init__(self):
		super(CalcCommand, self).__init__()
		self.__mathParser = MathStringParser()


	def run(self, message):
		return self.__mathParser.eval(message.content)


commandClass = CalcCommand