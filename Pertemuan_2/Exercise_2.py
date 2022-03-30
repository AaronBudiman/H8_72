massa = int(input('Masukan Berat Badan Kamu : '))
tinggi = int(input('Masukan Tinggi Badan Kamu : '))
imt = massa / (tinggi/100)**2

print ('Massa {} kg'.format(massa) + ' dan tinggi {} m'.format(tinggi/100))
print ('IMT = {}'.format(imt))

if imt < 18.5:
    print ('Berat Badan Kurang')
elif imt > 18.4 and imt < 25:
    print ('Berat Badan Ideal')
elif imt > 24.9 and imt < 30:
    print ('Berat Badan Berlebih')
elif imt > 29.9 and imt < 40:
    print ('Berat Badan Sangat Berlebih')
else : 
    print ('Obesitas')