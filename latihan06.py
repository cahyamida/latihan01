def HelloWorld(name):
    print("Hello, %s" % name)
    print(f"Hello,{name}")


HelloWorld("Luke Skywalker")


def seconFunc():
    name = 'Luke skywalker'
    return HelloWorld(name)

# print bilangan negatif


def printNegative(index, length):
    if index == "" and length == "":
        return  

    while index < length:
        if index % 2 == 1:
           print(index)
        index = + 1

# call method
helloWorld('John Doe')

seconFunc()

printNegative(0, 10)
