import json

class JsonReader():

    def getServerKey(self):
        config = {}
        try:
            files = open("./key.json")
            config = json.load(files)
            files.close()
        except Exception as e:
            print("Couldn't load json")

        return config['key']
