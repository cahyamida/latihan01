numbers = []
strings = []
names = ["Anakin Skywalker", "Padme Amidala", "Han Solo", "Qui-Gon Jinn", "Luke Skywalker", "Obi-Wan Kenobi"]

# write
 second_name = 1
 
 numbers.append(1)
 numbers.append(2)
 numbers.append(3)
  
 strings.append('Satu');
 strings.append('Dua');
 strings.append('Tiga');
 
 # this code should write out the filled arrays and the second name in the names list (Padme Amidala).
print(numbers)
print(strings)
print("The Second name on the names list is %s" % names[second_name])


#print the list variable use for
for i in names:
	print(i)

#print the list without name "Han Solo"
for x in names:
	if x!="Han Solo"
	print(x)
	
	or
for x in names:
	if x == "Han Solo":
	continue
	print(x)
