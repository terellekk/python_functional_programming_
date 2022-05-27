
class Person:
    
    def __init__(self, name, age=int, gender=str):
        self.name = name
        self.age = age 
        self.gender = gender
    
    def speak(self):
        print(f'Hello my name is {self.name}')

Jack = Person("Terelle",26,"Male")

Jack.speak()
