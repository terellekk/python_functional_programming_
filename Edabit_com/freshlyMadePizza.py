class Pizza:
    
    def __init__(self, ingredients, order_number = None):
        # self.order_number = None # how do we stop this from being a parameter
        self.order_number = order_number
        self.ingredients = ingredients

    # @classmethod
    # def ingredients(self):
    #     self.ingredients = ingredients
    # #    nested_dict = {1: {'name': 'haiwan', 'ingredients': self.ingredients},
    # #       2: {'name': 'meat_festival', 'ingredients': self.ingredients}
    # #       3: {'name': 'garden_feast', 'ingredients': self.ingredients}}
    #     return Pizza    

    class pizza_flavours(Pizza):
        def __init__(self, ingredients):
            Pizza.__init__(self, ingredients)
            flavours = {1: {'name': 'haiwan', 'ingredients': self.ingredients},
            2: {'name': 'meat_festival', 'ingredients': self.ingredients}
            3: {'name': 'garden_feast', 'ingredients': self.ingredients}}




p1 = Pizza(["bacon", "parmesan", "ham"])

print(p1.ingredients)



