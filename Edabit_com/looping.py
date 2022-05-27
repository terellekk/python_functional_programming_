'''Create a function that takes a list of numbers. Return the largest number in the list.


ex: findLargestNum([4, 5, 1, 3]) ➞ 5

Expect either positive numbers or zero (there are no negative numbers).
'''

# def findLargestNum(nums):
#     for i in nums:
#         return max(nums)
# findLargestNum([4, 5, 1, 3])


'''Create a function that takes a list of numbers and returns the smallest number in the list.
ex: find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999]) ➞ -0.9999
Test cases contain decimals.
'''
# def find_smallest_num(lst):
#     for i in lst:
#         return min(lst)
# find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999])

'''
Create a function that takes a number (from 1 - 60) and returns a corresponding string of hyphens.
ex: num_to_dashes(5) ➞ "-----"
You will be provided integers ranging from 1 to 60
'''

# def num_to_dashes(num):
#     for i in range(60):
#         return num * "-"
# num_to_dashes(5)

'''Mubashir created an infinite loop! Help him by fixing the code in the code tab to pass this challenge.
Look at the examples below to get an idea of what the function should do.
print_list(6) ➞ [1, 2, 3, 4, 5, 6]

READ EVERY WORD CAREFULLY, CHARACTER BY CHARACTER!
'''
#My attempt
# def print_list(n):
#     i = 0
#     while i < n:
#         i+= 1
#         return ([n])
# print_list(6)

# def print_list(n):
#     result = []
#     i = 1
#     while i <= n:
#         result +=[i]
#         i+=1
#         return result


# def print_list(n):
# 	result=[]
# 	i=1
# 	while i<=n:
# 		result+=[i]
# 		i += 1
# 	return result

'''Write a function that takes an integer and returns a string with the given number of "a"s in Edabit.

ex: how_many_times(5) ➞ "Edaaaaabit"

The string must start with "Ed" and end with "bit".
'''

# def how_many_times(num):
#         return f"Ed{(num * 'a')}bit" 

# how_many_times(5)

'''
Create a function that returns True if all parameters are truthy, and False otherwise.

ex: all_truthy(5, 4, 3, 2, 1, 0) ➞ False

Truthy values include non-empty sequences, numbers (except 0 in every numeric type), 
and basically every value that is not falsy.
You can check if an item is truthy by using an if statement on that item.
You will always be supplied with at least one parameter.

'''

# def all_truthy(*args):
#     truthy = True
#     if sum (args) == True:
#         return 'True'
#     else:
#         return 'False'
        

# all_truthy(5,4,3,2,1,0)

'''
Create a function that takes a list and a string as arguments and returns the index of the string.
find_index(["Red", "blue", "Blue", "Green"], "blue") ➞ 1

Don't forget to return the result.
The variable for list is lst, not 1st.
'''

# def find_index(lst,txt):
#     for i in (lst):
#         return (lst).index(txt)

# find_index(["Red", "Blue", "blue", "Green"], "blue")

'''

Create a function that takes a list and finds the integer which appears an odd number of times.
find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5
'''

def find_odd(lst):
    for i in (lst):
        print (lst.count(i))


find_odd([20,1,1,2,2,3,3,5,5,4,20,4,5])