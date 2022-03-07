import random

'''
Dice Rolling Simulator in Python: Examples
throw[y/n]:y
result: 5

throw[y/n]:n
end
max:
'''

def double_dice():
    
    #begin game
    game_start = input("Do you want to play? \n Type Yes or No ")
    #range of numbers

    dice = random.randint(1, 6)

    if game_start == 'Yes':
        print(f"Rolling dice...{dice} \n")

    else: 
        exit()

double_dice ()
