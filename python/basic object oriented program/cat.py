# blueprint
class Cat:
    # solid attributes
    leg = 4

    # initilize(method) changable attributes

    def __init__(self, name, breed, hair, age, gender, price):
        self.name = name
        self.breed = breed
        self.hair = hair
        self.age = age
        self.gender = gender
        self.price = price
        self.isHungry = True
        self.isSleepy = True

    def __str__(self):
        return f'Name:{self.name}\n  Breed:{self.breed}\n  Hair:{self.hair}\n  Age:{self.age}\n  Genger:{self.gender}\n  Price:{self.price} dollars'

    def __eq__(self, other):
        return self.breed == other.breed or self.hair == other.hair

    # behaviors(method only for objects)
    # every method must have argument self inside of the class
    def hunt(self):
        if self.isHungry:
            print(f'{firstCat.name} is gonna catch mouses.')
            self.isHungry = False
        else:
            print(f'{firstCat.name} is gonna stay at home.')

    def sleep(self):
        if self.isSleepy:
            print(f'{firstCat.name} is gonna sleep.')
            self.isSleepy = False
        else:
            print(f'{firstCat.name} is gonna play with his owner.')


print(f'Every cat has {Cat.leg} legs.')
# create object(instance)
firstCat = Cat('Ginger', 'Orange Cat', 'domestic short hair', 3, 'male', 150)
secondCat = Cat('Grey', 'American Short Hair Cat',
                'domestic short hair', 0.5, 'female', 150)
thridCat = Cat('Sherry', 'RagDoll', 'domestic short hair', 2.5, 'female', 4000)
print(f'name:{firstCat.name}\nbreed:{firstCat.breed}\nhair:{firstCat.hair}\nage:{firstCat.age}\ngender:{firstCat.gender}')
firstCat.hunt()
firstCat.hunt()
firstCat.sleep()
firstCat.sleep()

# market
class Dealership:
    def __init__(self):
        self.cats = []

    # interate the list
    def __iter__(self):
        yield from self.cats

    # add cats to the list
    def addCat(self, cat):
        self.cats.append(cat)


print()
deal = Dealership()
deal.addCat(firstCat)
deal.addCat(secondCat)
deal.addCat(thridCat)
for index, c in enumerate(deal, 1):
    print(f'{index}.{c}')
    print()

print()
if firstCat == secondCat:
    print(f'{firstCat.name} and {secondCat.name} are {firstCat.hair}')