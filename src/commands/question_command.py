from . command import *
from modules.wolframalpha import *


class QuestionCommand(Command):

	def __init__(self, config):
		super(QuestionCommand, self).__init__(config)
		self.__wolframAlpha = WolframAlpha(config['wolframalpha']['key'])


	def run(self, message):
		return self.__wolframAlpha.question(message.content)


commandClass = QuestionCommand