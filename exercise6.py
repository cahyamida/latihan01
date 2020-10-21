# Buat class mobil dgn atribut max_speed dan mileage
class Car(object):
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

carX = Car (240, 180)
print(f"Kecepatan:{carX.max_speed}, Mileage:{carX.mileage}")

# def get_data(self):
# print(f'{self.real}+{self.imag}')

#carX = Mobil(240, 180)
#print(carX.max_speed, carX.mileage)
