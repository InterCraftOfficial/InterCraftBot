import wolframalpha
import pprint
import json

class WolframAlpha:

	def __init__(self, appId):
		self.__client = wolframalpha.Client(appId)
		self.__prettyPrinter = pprint.PrettyPrinter()
		self.__pp = self.__prettyPrinter.pprint


	def question(self, query):

		if len(query.strip()) == 0:
			return "Ask me a question."

		try:
			response = self.__client.query(query.strip())
		except Exception:
			return "Help! Tell SirDavidLudwig or Raine to fix me!"

		if response['@success'] == 'true':
			# Print the response to the terminal for debugging purposes
			try:
				json.dumps(response, indent=4)
			except Exception as e:
				print(response)

			# Search for primary pod
			for pod in response['pod']:
				if "@primary" in pod and pod["@primary"] == "true":
					if type(pod['subpod']) == list:
						return pod['subpod'][0]['plaintext']
					else:
						return pod['subpod']['plaintext']

			print("No primary found")
			return response['pod'][0]['subpod']['plaintext']

		elif '@timedout' in response:
			return "I cannot tell unfortunately."

		return "I'm sorry, I don't understand what you are asking me here."
