jumlahHari = int(input('Jumlah Hari : '))

#menentukan Tahun
tahun = jumlahHari // 360

#sisa hari yang tersisa setelah penghitungan tahun
sisaHariBulan = jumlahHari % 360
bulan = sisaHariBulan // 30

#sisa hari yang tersisa setelah penghitungan bulan
sisaHariMinggu = sisaHariBulan % 30
minggu = sisaHariMinggu // 7

#sisah hari yang tersisa setelah penghitungan minggu
sisaHari = sisaHariMinggu % 7

print (str(jumlahHari) + ' Hari = ' + '{} Tahun'.format(tahun) + ', {} Bulan'.format(bulan) + ', {} Minggu'.format(minggu) + ', {} Hari'.format(sisaHari))
