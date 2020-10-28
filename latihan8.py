# Class & Object
"""
class ComplexNumber:
    glbl = 'Hello'
    # class constructor

    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}')


num1 = ComplexNumber(2, 3)

num1.get_data()
print(num1.glbl)
"""

# 22 okt 2020
# First Class

class Car:
    def __init__(self, maxSpeed=0, mileage=0):
        self.maxSpeed = maxSpeed
        self.mileage = mileage

    def getMaxSpeed(self):
        return self.maxSpeed

    def getMileage(self):
        return self.mileage

# Second class
class Toyota(Car):

    def __init__(self, model=None, color=None):
        self.model = model
        self.color = color
    
    def getModel(self):
        return self.model

    def getColor(self):
        return self.color
        
# method decorator
    @classmethod
    def getOwner(cls):
        print('This is the owner...')

toyo = Toyota ("Camry", "Black")

print (toyo.model)

toyo.maxSpeed = 200
 
print(toyo.getMaxSpeed())

Toyota.getOwner()







#instance class
carX = Car(300,1000)

#call property
print(f"max speed: {carX.getMaxSpeed()} Kmh")

print(carX.getMileage())

carY = Car(150, 500)

print(f"max speed: {carY.getMaxSpeed()} Kmh")
print(f"Mileage: {carY.getMileage()} Km")
