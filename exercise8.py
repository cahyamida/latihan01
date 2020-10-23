#Dictionaries
phone ={
    "John": 812312,
    "Jack": 981231,
    "Doe": 7123342,
}
print(phone)

phonebook ={
    "name": "Luke Skywalker",
    "role": "Jedi",
    "email": "luke@mail.com"
},
{
   "name": "Padme",
    "role": "Princess",
    "email": "padme@mail.com",
},
{
   "name": "Han Solo",
    "role": "Pilot",
    "email": "Han@mail.com",
}
print(phonebook)

phone = {"John Doe": 218998989, "Max": 277799999}

for i, v in phone.items():
    print(f"Name:{i}, Phone:{v}")
    print("%s %s "% (i,v))


dict1 = phone.pop("John Doe")
print(dict1)

#Tuple
tp =("Kambing", "Kerbau", "Sapi")
print(tp)
ls = list(tp)
ls[0] = "Kucing"
print(ls)

tp = ("Draft", "Progress", "Done")
print(tp)
ls= list(tp)
print(ls)

#it tp == ls:
print(ls)

x1 = [1,2,3]
x2 = x1

if x1 == x2:
    print("True")
if x1 is x2:
    print ("True")
