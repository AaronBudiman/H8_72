apelPrice = 10000
jerukPrice = 15000
anggurPrice = 20000

inputApel = int(input('Jumlah Apel yang mau dibeli :' ))
inputJeruk = int(input('Jumlah Jeruk yang mau dibeli :'))
inputAnggur = int(input('Jumlah Anggur yang mau dibeli :'))

totalPriceApel = apelPrice * inputApel
totalPriceJeruk  = jerukPrice * inputJeruk
totalPriceAnggur = anggurPrice * inputAnggur
totalPrice = totalPriceApel + totalPriceJeruk + totalPriceAnggur

print ('Detail Belanja')
print ('Apel : ' + str(inputApel) + ' x ' + str(apelPrice) + ' = ' + str(totalPriceApel))
print ('Jeruk : ' + str(inputJeruk) + ' x ' + str(jerukPrice) + ' = ' + str(totalPriceJeruk))
print ('Anggur : '+ str(inputAnggur) + ' x ' + str(anggurPrice) + ' = ' + str(totalPriceAnggur))

print ('Total : ' + str(totalPrice))

uangMasuk = int(input('Masukan Jumlah Uang :'))

uangKembali = uangMasuk - totalPrice

if uangKembali < 0:
    print ('Transaksi Anda DIbatalkan')
    print ('Uang anda kurang : {}'.format(-uangKembali))
elif uangKembali == 0:
    print ('Terima Kasih')
else :
    print ('Terima Kasih')
    print ('Uang Kembali Anda : {}'.format(uangKembali))