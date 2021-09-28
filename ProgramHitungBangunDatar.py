#PROJECT KALKULATOR BANGUN DATAR
#identifikasi :
#p = panjang
#l = lebar
#s = panjang sisi
#r = Jari-Jari lingkaran
#L = Hasil Luas Bangun
#K = Hasil Keliling Bangun
#menu_bangun = pilihan bangun datar
#menu_operasi = pilihan operasi bangun

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
def persegipanjang(operasi):
    print('--------------------------------')
    print('--------------------------------')
    if operasi==1:
        #luas persegi panjang
        print('Perhitungan Luas Persegi Panjang')
        p=int(input('Masukan panjang persegi panjang :'))
        l=int(input('Masukkan Lebar persegi panjang :'))
        L =p*l
        print ('Luas Persegi panjangnya adalah =' + str(L)+'cm')
    elif operasi==2:
        #keliling persegi panjang
        print('Perhitungan Keliling Persegi Panjang')
        p=int(input('Masukan panjang persegi panjang :'))
        l=int(input('Masukkan Lebar persegi panjang :'))
        K=2*(p+l)
        print ('Keliling Persegi panjangnya adalah ='+str(K)+'cm') 
    else :
        print('Masukan Salah, silahakan ulangi')

print('[KALKULATOR LUAS DAN KELILING BANGUN DATAR]')
print('-------------------------------------------')
print('Menu Bangun :')
print('1. Persegi Panjang')
print('2. Persegi')
print('3. Lingkaaran') 
print('4. Keluar')
menu_bangun=int(input('Masukkan jenis bangun datar diinginkan : '))
print('-------------------------------------------')
print('Menu Perhitungan:')
print('1. Luas')
print('2. Keliling')
print('3. Keluar')
menu_operasi=int(input('Masukkan jenis perhitungan yang diinginkan :'))
