# Class & Object
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
