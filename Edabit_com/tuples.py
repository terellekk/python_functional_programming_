# mytuple = ["Terelle", "Seyi", "John", "Alfred"]

# for elem in mytuple:
#     if elem == 'Seyi':
#         print(elem.lower())

#####Amazon application
####cart systems

def create_list():
    user_list = []
    return user_list


def add_to_list(user_cart, item):
    user_cart.append(item)
    return user_cart

def remove_from_cart(user_cart,item):
    user_cart.remove(item)
    return user_cart

def clear_all(user_cart):
    user_cart.clear()
    return user_cart

def display_cart(user_cart):
    cart_display = {}
    for i in range(len(user_cart)):
        it = f'item {i+1}'
        value = user_cart[i]
        cart_display[it] = value
    return cart_display

def add_item
wait = True
user_cart = create_list()
while wait == True:
    next_item = input("What item would you like to addd? enter end to exit input")
    if next_item == 'end':
        wait = False
    else:
        updated_cart = add_to_list(user_cart, next_item)

#######
# user_cart = create_list()
# updated_cart = add_to_list(user_cart, 'apple')
# cart_view = display_cart(updated_cart)
# print(cart_view)
# updated_cart = remove_from_cart(updated_cart, 'apple')
# cart_view = display_cart(updated_cart)
# print(cart_view)