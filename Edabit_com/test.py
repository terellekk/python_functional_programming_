class Dog:
    Location = 'TEXAS'
    def __init__(self, name, age):
        self.dog_name = name
        self.dog_age = age
    
    def describe(self):
        print(f'This dog named {self.dog_name} with age {self.dog_age} is from {self.Location}')

    @classmethod
    def describe2(cls, Location):
        print(f'This dog named {cls.dog_name} with age {cls.dog_age} is from {cls.Location}')


d1 = Dog('hack', 12)
d1.describe()
