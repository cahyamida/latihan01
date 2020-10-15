astring = "Hello world my name is Luke"

print(astring.index("o"))

print(astring.count("l"))

#[start:stop:step]
astring = "Hello world my name is Luke"
print(astring[3:7:2])
print(astring[::-1])
print(astring.upper())
print(astring.lower())

#split
astring = "Hello world!"
afewwords = astring.split(",")
print("Split sample %s " %astring.split(" "))

#condition
x = 2
if x == 2:
	print(x)
if "Hello" in alist:

	print("yes I have")		
	print(len(alist))
#if and else
#if <condition> :
	statement
#elif <condition> :
	statement
#else :
	statements
# The is operator
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False
print(not false) # Prints out True
print((not false) == (False)) # Prints out False
