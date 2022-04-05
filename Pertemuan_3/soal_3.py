apelPrice = 10000
jerukPrice = 15000
anggurPrice = 20000

stockApel = 20
stockJeruk = 15
stockAnggur = 25

listIndex = ['Index', '0', '1', '2']
listBuah = ['Nama', 'Apel', 'Jeruk','Anggur']
listStock = ['Stock', '10', '15', '20']
listHarga = ['Harga', '10000', '15000', '20000']

kartBuah = ['Nama']
kartQty = ['Qty']
kartHarga = ['Harga']
kartTotal = ['Total Harga']

##buat bikin daftar buah cantik tanpa perlu ketik ulang
def daftarBuah():
    print('DaftarBuah')
    print('')
    for i in range(len(listIndex)):
            print(listIndex[i] + ' '*(len(listIndex[0])-len(listIndex[i]))+' | ' + listBuah[i] + ' '*(len(max(listBuah, key=len))-len(listBuah[i])) + ' | ' + listStock[i] + ' '*(len(max(listStock, key=len))-len(listStock[i])) + ' | ' + listHarga[i])

def daftarKart():
    print('Isi Kart:')
    for j in range(len(kartBuah)):
            print(kartBuah[j] + ' '*(len(max(kartBuah, key=len))-len(kartBuah[j])) + ' | ' + kartQty[j] + ' '*(len(max(kartQty, key=len))-len(kartQty[j])) + ' | ' + kartHarga[j])

listMenu = ['1. Menampilkan Daftar Buah', '2. Menambah Buah', '3. Menghapus Buah', '4. Membeli Buah' ,'5. Exit Program']

inputMenu = 0

while inputMenu < 5:
    print('')
    print('Selamat Datang di Pasar Buah')
    print('')
    print('List Menu :')
    for x in listMenu:
        print(x)

    inputMenu = int(input('Masukan Menu yang anda Ingin Jalankan : '))
    print('Masukan Menu yang anda Ingin Jalankan : {}'.format(listMenu[inputMenu-1]))

## Menu 1
    if inputMenu == 1:
        daftarBuah()

#### halaman 2
    elif inputMenu == 2:
        tambahBuah = input('Masukan Nama Buah : ')
        tambahStock = input('Masukan Stock Buah : ')
        tambahHarga = input('Masukan Harga Buah : ')
        indexNumber = len(listIndex)
        tambahIndex = int(indexNumber-1)
        listIndex.append(str(tambahIndex))
        listBuah.append(str(tambahBuah))
        listStock.append(str(tambahStock))
        listHarga.append(str(tambahHarga))
        daftarBuah()

## halaman 3
    elif inputMenu == 3:
        daftarBuah()
        print('')
        buangIndex = int(input('Masukan Index Buah yang ingin dihapus : '))
        print('')
        indexDel = buangIndex + 1
        listIndex.pop()
        del listBuah[indexDel]
        del listStock[indexDel]
        del listHarga[indexDel]
        daftarBuah()

## halaman 4
    elif inputMenu == 4:
        daftarBuah()
        belanjaLanjut = 'ya'
        lanjut = 'ya'
        while belanjaLanjut == lanjut:
            kartIndex = int(input('Masukan Index Buah yang ingin dibeli : '))
            stockMasukKart = int(input('Masukan jumlah yang ingin dibeli : '))
            if stockMasukKart > int(listStock[kartIndex+1]):
                print('Stock tidak cukup, stock {}'.format(listBuah[kartIndex+1]) + ' tinggal {}'.format(listStock[kartIndex+1]))
                daftarKart()
            else:
                kartBuah.append(str(listBuah[kartIndex+1]))
                kartQty.append(str(stockMasukKart))
                kartHarga.append(str(listHarga[kartIndex+1]))
                daftarKart()
            belanjaLanjut = input('Mau beli yang lain? (ya/tidak) :')
        else :
            for k in range(len(kartBuah)-1):
                a = k + 1
                indexKartQty = a 
                indexKartHarga = a 
                kartTotal.append(str(int(kartQty[indexKartQty]) * int(kartHarga[indexKartHarga])))
            for j in range(len(kartBuah)):
                print(kartBuah[j] + ' '*(len(max(kartBuah, key=len))-len(kartBuah[j])) + ' | ' + kartQty[j] + ' '*(len(max(kartQty, key=len))-len(kartQty[j])) + ' | ' + kartHarga[j] + ' | ' + kartTotal[j])
            totalHarga = sum(map(int, kartTotal[1:]))
            print('Total Yang Harus Dibayar = {}'.format(totalHarga))
            uangMasuk = int(input('Masukan Jumlah Uang = '))
            print('Terima Kasih')
            print('')
            print('Uang Kembali Anda = {}'.format(uangMasuk-totalHarga))
            break

## halaman 5
    else :
        print('Selamat Tinggal')


