'''
Write a function that takes a positive integer num and calculates
how many dots exist in a pentagonal shape around the center dot
on the Nth iteration.

In the image below you can see the first iteration is only a single
dot. On the second, there are 6 dots. On the third, there are 16 dots,
and on the fourth there are 31 dots.


Return the number of dots that exist in the whole pentagon on the Nth
iteration.


pentagonal(1) ➞ 1

pentagonal(2) ➞ 6

'''


def pentagonal(num):
    return   num*(3*num - 1) / 2

pentagonal(2)

def pentagonal(num):
    sum = 1
    i = 3
    sum += (5*(num-1))
    while i <=num:
        i+=1
        sum += (5*(i-2))
	
    return sum

pentagonal(1)