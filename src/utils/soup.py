

class Soup():

    def __init__(self):
        self.__ingredients = {}

    def addIngredient(self, ingredient):
        try:
            self.__ingredients[ingredient] += 1
        except Exception as e:
            self.__ingredients.update({ingredient : 1})


    def checkIngredient(self, ingredient):
        return self.__ingredients[ingredient]

    def getStatus(self):
        return list(self.__ingredients.keys())
