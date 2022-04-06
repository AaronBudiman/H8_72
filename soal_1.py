list1 = [1,2,3,4,5]
list2 = [22,17,19,20,14]
list3 = [1,3,5]
list4 = [2,4,6]
newList = []

def genap(angka):
    return angka % 2 == 0

hasilMap = map(genap, list2)
hasilListMap = list(hasilMap)

for i in hasilListMap:
    newList.append('Genap' if i == True else 'Ganjil')

print(list2)
print(newList)