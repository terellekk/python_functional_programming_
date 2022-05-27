class CoffeeShop:
    menu_options = {
    Food: {'Bagel':1.20, 'Eggs':0.80},
    Drinks:{'Orange Juice': 4.00, 'Apple Juice': 4.80}
    }

    def __init__(self, name, menu, orders):
        self.name = name
        self.menu = menu
        self.orders = orders

    
    def add_order(self): 
        order_list = []
        '''adds the name of the item to the end of the orders list if it exists on the menu,
         otherwise, return "This item is currently unavailable!"'''
        for i in menu_options:
            if i == CoffeeShop.menu:
                order_list.append(i)
            else:
                return None

    def fulfill_order(self): 
        self.item
        '''if the orders list is not empty, return "The {item} is ready!". If the orders list
            is empty, return "All orders have been fulfilled!"'''
        if order_list != None:
            return f'The {item} is ready!'
        elif order_list == None:
            return f'All orders have been fulfilled!'

    def list_orders(self):
        '''returns the item names of the orders taken, otherwise, an empty list.'''
        if self.orders > 0:
            return CoffeeShop.items
        else:
            return []
            
    def due_amount(self):
         '''returns the total amount due for the orders taken.'''


    def cheapest_item(self):
        '''returns the name of the cheapest item on the menu.'''

    def drinks_only(self):
        '''returns only the item names of type drink from the menu.'''


    def food_only(self):
        '''returns only the item names of type food from the menu.'''

        ##Dictionairy to pull name: price