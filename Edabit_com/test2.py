class Pizza:
    order_no_global = 1
    def __init__(self, ingredients):
        self.order_no = Pizza.order_no_global
        self.ingredients = ingredients
    
    @classmethod
    def garden_feast(self):
        Pizza.order_no_global += 1
        self.order_no = self.order_no_global
        self.ingredients = ['spinach', 'olives', 'mushroom']
        return Pizza

p1 = Pizza(["bacon", "parmesan", "ham"])
print(p1.ingredients)
print(p1.order_no)

p2 = Pizza.garden_feast()
print(p2.ingredients)
print(p2.order_no)


