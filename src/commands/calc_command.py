from . command import *
from modules.math_string_parser import *


class CalcCommand(Command):

	def __init__(self, config):
		super(CalcCommand, self).__init__(config)
		self.__mathParser = MathStringParser()


	def run(self, message):
		return self.__mathParser.eval(message.content)


commandClass = CalcCommand