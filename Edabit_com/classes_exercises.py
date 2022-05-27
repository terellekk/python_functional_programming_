# # '''
# # Create a method in the Person class which returns how another person's age
# #  compares. Given the objects p1, p2 and p3, which will be initialised with
# #   the attributes name and age, return a sentence in the following format:
# # {other_person} is {older than / younger than / the same age as} me.
# # '''
# # #Created Person class
# # class Person: 
# #     #initiliaising attributes
# #     def __init__(self, name, age):
# #         self.const_name = name
# #         self.const_age = age

# #     #age comparison
# #     def compare_age(self, other_class):
# #         if self.const_age > other_class.const_age:
# #             print(f'{self.const_name} is greater than {other_class.const_name}')

# # p1 = Person("Terelle", 26)
# # p2 = Person("Seyi", 23)

# # print(p1.const_age)
# # print(p2.const_age)
# # p1.compare_age(p2)



# '''
# Create methods for the Calculator class that can do the following:

# Add two numbers.
# Subtract two numbers.
# Multiply two numbers.
# Divide two numbers.
# Examples
# calculator = Calculator()

# calculator.add(10, 5) ➞ 15

# calculator.subtract(10, 5) ➞ 5

# calculator.multiply(10, 5) ➞ 50

# calculator.divide(10, 5) ➞ 2

# '''

# class Calculator:

#     def __init__(self):
#         pass

#     def add(self, num1, num2):
#         "This method returns the sum of 2 numbers"
#         return num1 + num2
    
#     def sub(self, num1, num2):
#         "This method returns the value of 1 number minus the second"
#         return num1 - num2

#     def mult(self, num1, num2):
#         "This method returns the value of 2 numbers, once multiplied"
#         return num1 * num2
    
#     def divide(self, num1, num2):
#         "This method returns the value of 2 numbers, once divided"
#         return num1 / num2


# calculator = Calculator()

# a = calculator.add(10, 5)

# print(a)    





#Magic characteristics
class Magic:
    #Constructor initiliasing self, doesn't take attr
    def __init__(self):
        pass

    #This method will replace strings with char, defined by user
    def replace(self, str1, str2, char1):
        return str1.replace(str2, char1)

    #This method will return the len() to user - come back to this
    def str_length(self, str3):
        return len(str3)

    #This method will remove leading and trailing spaces using strip()
    def trim(self, str4):
        return str4.strip()

     #This method will remove leading and trailing spaces using slice ()   
    def list_slice(self, list1, numbs):
        starting_no = numbs[0]
        ending_no = numbs[1]
        
        postion_starting_no = list1.index(starting_no)
        postion_ending_no = list1.index(ending_no)

        final_list_slicing = list1[postion_starting_no : postion_ending_no]

        return final_list_slicing






magic1 = Magic()

#creaated 3 instances
print(magic1.replace("AzErty-QwErty", "Ea", "e"))
#call both methods for each user
print(magic1.list_slice([1,2,3,4,5,6,7], (2,6)))








