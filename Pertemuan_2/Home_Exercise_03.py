apelPrice = 10000
jerukPrice = 15000
anggurPrice = 20000

stockApel = 6
stockJeruk = 7
stockAnggur = 6

inputApel = int(input('Jumlah Apel yang mau dibeli :' ))
while inputApel > stockApel:
    print ('Jumlah yang dimasukan terlalu banyak')
    print ('Stock Apel tinggal : {}'.format(stockApel))
    inputApel = int(input('Jumlah Apel yang mau dibeli :' ))
    
inputJeruk = int(input('Jumlah Jeruk yang mau dibeli :'))
while inputJeruk > stockJeruk:
    print ('Jumlah yang dimasukan terlalu banyak')
    print ('Stock Jeruk tinggal : {}'.format(stockJeruk))
    inputJeruk = int(input('Jumlah Jeruk yang mau dibeli :' ))

inputAnggur = int(input('Jumlah Anggur yang mau dibeli :'))
while inputAnggur > stockAnggur:
    print ('Jumlah yang dimasukan terlalu banyak')
    print ('Stock Anggur tinggal : {}'.format(stockAnggur))
    inputAnggur = int(input('Jumlah Anggur yang mau dibeli :' ))

print ('')

totalPriceApel = apelPrice * inputApel
totalPriceJeruk  = jerukPrice * inputJeruk
totalPriceAnggur = anggurPrice * inputAnggur
totalPrice = totalPriceApel + totalPriceJeruk + totalPriceAnggur

print ('Detail Belanja')
print ('')
print ('Apel : ' + str(inputApel) + ' x ' + str(apelPrice) + ' = ' + str(totalPriceApel))
print ('Jeruk : ' + str(inputJeruk) + ' x ' + str(jerukPrice) + ' = ' + str(totalPriceJeruk))
print ('Anggur : '+ str(inputAnggur) + ' x ' + str(anggurPrice) + ' = ' + str(totalPriceAnggur))
print ('')
print ('Total : ' + str(totalPrice))

bayar = int(input('Masukan Jumlah Uang : '))
while bayar < totalPrice:
    print ('Uang anda kurang sebesar {}.'.format(totalPrice-bayar))
    bayar = int(input('Masukan Jumlah Uang : '))
else :
    print ('Terima Kasih')
    print ('Uang Kembali Anda : {}'.format(bayar-totalPrice))
