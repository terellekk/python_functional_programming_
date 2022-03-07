'''
Make a Temperature/Measurement Converter.
Write a script that can convert Fahrenheit to Celcius and back, or inches to centimeters and back, etc. 
    How far ca you take it?
    max_days: 2hours
'''


def temp_converter():
   
   #This code takes user input, converts from a string to int, then converts user input to C or F

    user_temp = input("Do you want to convert Fahrenheit or Celcius? ")

    if user_temp == 'Fahrenheit':

        Fahrenheit = int(input("Enter a temperature in Fahrenheit: "))

        Celsius = (Fahrenheit - 32) * 5.0/9.0

        print (f"Temperature:", Fahrenheit, "Fahrenheit = ", Celsius, " C")
    
    else:
        user_temp == 'Celcius'

        Celsius = int(input("Enter a temperature in Celsius: "))

        Fahrenheit = 9.0/5.0 * Celsius + 32

        print ("Temperature:", Celsius, "Celsius = ", Fahrenheit, " F")

    user_input2 = input('Are you finished? \n [Y/N]\n')

    if user_input2 == 'Y':
        print('OK goodbye')
    while user_input2 == 'N':
        temp_converter()

temp_converter()
