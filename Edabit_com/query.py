from test import small_task

def main_interface():
    question = input("Do you want to find the cube root? Enter CR \n Do you want to find the square root? Enter SR \n Do you want to add? Enter ADD ").upper()
    if question == 'CR':
        try:
            present_number = int(input("What number do you want to cube root? "))
            result = small_task.cube_root(present_number)
            if result > 5:
                print('im greater than')
            else:
                print('ouch lower')
        except ValueError:
            print('Wrong number value given')
        
        #This will line be where we import the function
    elif question == 'SR':
        present_number = int(input("What number do you want to square root? "))
        print(small_task.square_root(present_number))
        #This will line be where we import the function
    elif question == 'ADD':
        present_number = int(input("First number you want to add? "))
        present_number1 = int(input("Second number you want to add? "))
        print(small_task.addition(present_number, present_number1))
        #This will line be where we import the function

main_interface()

        

