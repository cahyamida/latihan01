# latihan 05

# prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count+1

# Prints out 0,1,2,3,4,5
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# atau coba lagi
# Prints out 0,1,2,3,4,5
count = 0
while True:
    print('before: %d' % count )
    count += 1
    if count >= 5:
        break
