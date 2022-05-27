'''
Create a function that takes in a current mood and return a sentence in the following format:
 "Today, I am feeling {mood}". However, if no argument is passed, return "Today, I am feeling neutral".
'''

def mood_today(mood ="neutral"):
     return 'Today, I am feeling {}'.format(mood)
mood_today("happy") 