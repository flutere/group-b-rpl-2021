#PROJECT KALKULATOR BANGUN DATAR
#identifikasi :
#p = panjang
#l = lebar
#s = panjang sisi
#r = Jari-Jari lingkaran
#L = Hasil Luas Bangun
#K = Hasil Keliling Bangun

def persegi(operasi):
    print('--------------------------------')
    print('--------------------------------')
    if operasi==1:
        #luas persegi
        print('Perhitungan Luas Persegi')
        s=int(input('Masukkan panjang sisi persegi: '))
        L = s*s
        print ('Luas Perseginya adalah ='+str(L)+'cm')
    elif operasi==2:
        #kelliling persegi
        print('Perhitungan Keliling Persegi')
        s=int(input('Masukkan panjang sisi persegi: '))
        K = 4*s
        print ('Keliling Perseginya adalah ='+str(K)+'cm')
    else :
        print('Masukan Salah, silahakan ulangi')

print('[KALKULATOR PERSEGI]')
print('-------------------------------------------')
menu_keys=int(input('Mohon ketik angka 2 untuk memulai'))
print('-------------------------------------------')
print('Menu Perhitungan:')
print('1. Luas')
print('2. Keliling')
print('3. Keluar')
b=int(input('Masukkan jenis perhitungan yang diinginkan :'))

if menu_keys==1:
    print('Mohon ketik angka 2 untuk memulai')
elif menu_keys==2:
    persegi(b)
elif menu_keys==3:
    print('Mohon ketik angka 2 untuk memulai')
else :
    pass