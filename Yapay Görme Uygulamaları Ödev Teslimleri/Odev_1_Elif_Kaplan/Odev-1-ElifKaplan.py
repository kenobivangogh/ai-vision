# -*- coding: utf-8 -*-
'''
MEK713 Mekatronikte Yapay Görme Uygulamaları
Odev 1: Python Temel Yapilari
'''

'''
Ogrenci No: 1238137151
Adi Soyadi: Elif Kaplan
'''

# Odev 1: Asagidaki sorulari verilen dizi icin kodlayiniz.
# Her sorunun cevabini ilgili aciklama satirinin altina kodlayiniz.


dizi = [12,63,76,23,98,67,52,13,3,87,6,0,32,4,82,23,54,65,37,97,41]

# Soru 1: Tüm dizi elemanlarını ekrana yazdiriniz. 

print("Tüm dizi elemanları:")
print(*dizi, sep=" ")

# Soru 2: Sadece 50'den buyuk olan dizi elemanlarini ekrana yazdiriniz.
print("\n")
print("Dizideki 50'den büyük sayılar:")
for eleman in dizi:
    if eleman > 50:
        print(eleman, end=" ")

# Soru 3: Dizideki sadece tek sayilari ekrana yazdiriniz 

print("\n")
print("Dizideki tek sayılar:")
for eleman in dizi:
    if eleman % 2 != 0:
        print(eleman, end=" ")

# Soru 4: Dizideki sayilarin aritmetik ortalamasini ekrana yazdiriniz 
print("\n")
# Toplamı ve eleman sayısını başlangıçta sıfıra eşitliyoruz
toplam = 0
eleman_sayisi = 0

# Listenin her elemanını toplam değişkenine ekliyoruz
for eleman in dizi:
    toplam += eleman
    eleman_sayisi += 1

# Aritmetik ortalama hesaplanıyor
ortalama = toplam / eleman_sayisi

# Sonucu ekrana yazdırıyoruz
print("Dizinin aritmetik ortalaması:", ortalama)

# Soru 5: Dizideki sadece asal sayıları bulup ekrana yazdırınız 
print("\n")

def asal_mi(sayi):
    # 2 hariç 2'ye bölünebilen sayılar asal değildir
    if sayi == 2:
        return True
    if sayi < 2 or sayi % 2 == 0:
        return False
    # Kökünü alıyoruz ve 3'ten başlayarak tek sayıları kontrol ediyoruz
    for i in range(3, int(sayi**0.5) + 1, 2):
        if sayi % i == 0:
            return False
    return True

# Dizideki asal sayıları ekrana yazdırıyoruz
print("Dizideki Asal sayılar:")
for sayi in dizi:
    if asal_mi(sayi):
        print(sayi, end=" ")


