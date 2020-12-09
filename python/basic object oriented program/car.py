# blueprint
class Car:
    # car attributes
    # something is solid for the object
    wheels = 4
    doors = 2
    engine = True

    # initialize the attribute inside of the class
    # default make
    # each object in the same class can have different attributes
    # inside of the class, called method
    # every method in the class need self argument
    def __init__(self, model, year, make='Honda'):
        self.make = make
        self.model = model
        self.year = year
        self.gas = 100
        self.isMoving = False

    # other dunder method
    def __str__(self):
        return f'{self.make} {self.model} {self.year}'

    def __eq__(self,other):
        return self.make == other.make and self.model == other.model

    def stop(self):
        if self.isMoving:
            print('The car has stopped.')
            self.isMoving = False
        else:
            print('The car has already stopped')

    def go(self, speed):
        if self.useGas():
            if not self.isMoving:
                print('The car starts moving')
                self.isMoving = True
            print(f'The car is going {speed}')
        else:
            print('you have run out of gas')
            self.stop()

    def useGas(self):
        self.gas -= 50
        if self.gas <= 0:
            return False
        else:
            return True

# change class attribues would not affect the change of instance attribute
# car dealership


class Dealership:
    def __init__(self):
        self.cars = []

    # use iter method to iterate attributes
    def __iter__(self):
        yield from self.cars
    
    def addCar(self, car):
        self.cars.append(car)


carOne = Car('Accord', 2015)
carTwo = Car('Accord', 2019)
carThree = Car('Sport', 2010,)
carOne.go('slow')
carOne.go('fast')
carOne.stop()
carOne.stop()
print(str(carOne))

print()
print()
print("Iterate attributes:")
myDealership = Dealership()
myDealership.addCar(carOne)
myDealership.addCar(carTwo)
myDealership.addCar(carThree)
for car in myDealership:
    print(car)

if carOne == carTwo:
    print("They are equal")
else:
    print("They are not equal")
