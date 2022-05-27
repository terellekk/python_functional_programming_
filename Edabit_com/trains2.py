class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

def manage_dogs(objects,name,age):
    if objects.name == 'bingo':
        objects.age = 2

dog1 = Dog('bingo', 10)
dog2 = Dog('suave',20)
dog3 = Dog('ave',30)

dogs_ = [dog1,dog2, dog3]

# for item in dogs_:
#     # print(item.name)
#     manage_dogs(item, 'bingo',None)
manage_dogs(dogs_[0],'bingo', None)
manage_dogs(dogs_[1],'bingo', None)
manage_dogs(dogs_[2],'bingo', None)

print('new age',dogs_[0].age)

