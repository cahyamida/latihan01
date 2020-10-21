# buat function menampilkan urutan bilangan yang habis dibagi 3 dengan argument range.

# def bilangan3(baris = None):
#   if baris == None or baris < 3:
#      return
# for bil in range(baris):
#    if bil == 0:
#       continue
#  if bil % 3 == 0:
#     print(bil)

# bilangan3(100)
# bilangan3()

def bilangan3(baris=None):
    if baris == None or baris < 3:
        return
    index = 1
    while index < (baris):
        if index == 0:
            continue
        if index % 3 == 0:
            print(index)
        index += 1


# call function
bilangan3(25)
