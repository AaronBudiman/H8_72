def mapDuplikat (fn, collection):
    newCollection = []
    for item in collection:
        newCollection.append(fn(item))

    return newCollection

list1 = [2, 4, 6, 8, 10]

def ubah(angka):
    return 'Angka {}'.format (angka)

newList = mapDuplikat(ubah, list1)
print (newList)

