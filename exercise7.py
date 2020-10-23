# Buat 1buah class parent apapun dengan minimal 2 atribute
# Buat 1buah class child dari class parentnya

#first class
class Coffee:
    def __init__(self, bean=None, roasted=None):
        self.bean = bean
        self.roasted = roasted

    def getBean(self):
        return self.bean

    def getRoasted(self):
        return self.roasted

#Second class
class Arabica(Coffee):

    def __init__(self, color=None, origin=None):
        self.color = color
        self.origin = origin
    
    def getColor(self):
        return self.color

    def getOrigin(self):
        return self.origin

    @classmethod
    def getOwner(cls):
        print('Java Preanger specialty is Arabica green bean')

coffee = Arabica ("color", "origin")
print(coffee.getColor())
coffee.color="Green"
print(coffee.getColor())
Arabica.getOwner()


#dicoba dr yg punya kang Candra 
##first class
class Cemilan(object):
#  makanan enak buat ngemil
    def __init__(self, nama=None, bahan=None):
        self.nama = nama
        self.bahan = bahan

    def getNama(self):
        return self.nama
    
    def getBahan(self):
        return self.bahan

#second class
class Rasa(Cemilan):
    def __init__(self, rasa=None, tekstur=None):
        self.rasa = rasa
        self.tekstur = tekstur
        super().__init__(rasa, tekstur, nama, bahan)
        
    def getRasa (self):
        return self.rasa
    
    def getTekstur (self):
        return self.tekstur

#instansiasi
mieSetan = Rasa ("Pedas, Renyah")

print(mieSetan.getRasa())

mieSetan.nama = "Terigu"

cemilan1 = Cemilan("Odading", "terigu")
rasa1 = Rasa("anjiimm banget", "gurih bangeed")
print ("Nama Cemilan : %s"% cemilan1.namaCemilan())
print ("Bahan Cemilan : %s"% cemilan1.bahanCemilan())
print("Rasanya : %s"% rasa1.CitaRasa())
print("Teksturnya :%s"% rasa1.teksturNya())
rasa1.nama = "JEding"
print(rasa1.namaCemilan())








