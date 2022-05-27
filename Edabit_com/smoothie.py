class Smoothie:

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def get_cost(self):
        total_cost = 0
        strawberries = 	1.50
        banana = 0.50
        mango = 2.50
        raspberries = blueberries = 1.00
        apple = 1.75
        pineapple = 3.50
        
        for ingredient in self.ingredients:
            if ingredient == 'banana':
                total_cost += banana
            elif ingredient == 'strawberries':
                total_cost += strawberries
            elif ingredient == 'mango':
                total_cost += mango
            elif ingredient == 'raspberries' or 'blueberries':
                total_cost += raspberries or blueberries
            elif ingredient == 'apple':
                total_cost += apple
            elif ingredient == 'pineapple':
                total_cost += pineapple
                return total_cost

    def get_price(self):
        return (round(self.get_cost *1.5, 2))
    
    def get_name(self):
       for ingredients_listed in self.ingredients:
           if any (ingredients_listed.replace("berries", "berry")):
                if len(self.ingredients) > 1:
                    a = self.ingredients.sort()
                    return f'{a} Fusion'
                elif len(self.ingredients) < 2:
                    b = self.ingredients.sort()
                    return f'{b} Smoothie'   


s1 = Smoothie(["banana"])

print(s1.get_cost)
