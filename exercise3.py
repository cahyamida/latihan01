# Exercise 3 : buat baris bilangan genap dan ganjil 1-10.
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# or
for x in range(1, 11):
    if x % 2 == 1:
        print(x)

# While Loops
ls = [1, 5, 6, 10, 2]
index = 0
while index < len(ls):
    print(ls[index])
    index += 1

#FUNCTION / METHODS
