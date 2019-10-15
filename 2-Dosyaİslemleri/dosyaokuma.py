# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
Dosya Okuma
"""
# dosya açma
dosya = open("ogrenciler", "r")

# dosyanın tamamı okunsun
dosya_icerik = dosya.read()
print(dosya_icerik)
dosya.close()

dosya = open("ogrenciler", "r")
dosya_liste = dosya.readlines()
print(dosya_liste)
print("satır sayısı", len(dosya_liste))
dosya.close()

dosya = open("ogrenciler", 'r')
dosya_satir = dosya.readline()
print(dosya_satir)
dosya.close()