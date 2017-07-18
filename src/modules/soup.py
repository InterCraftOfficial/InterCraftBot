import inflect

class Soup():

    def __init__(self):
        self.__ingredients = {}
        self.__inflect = inflect.engine()


    def addIngredient(self, ingredient, quantity=1):
        if self.__inflect.singular_noun(ingredient):
            ingredient = self.__inflect.singular_noun(ingredient)

        try:
            self.__ingredients[ingredient] += quantity
        except Exception as e:
            self.__ingredients.update({ingredient : quantity})


    def ingredientCount(self, ingredient):
        return self.__ingredients[ingredient]


    def ingredients(self):
        return list(self.__ingredients.keys())
