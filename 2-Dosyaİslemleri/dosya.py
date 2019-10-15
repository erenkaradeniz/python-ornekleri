# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
Dosya işlemleri
"""
"""
* iki tür dosya çeşidi vardır: binary ve metin dosyaları
* open() : geriye bir dosya nesnesi döndürür.
* okuma işlemini yapan metotlar
* read() : bütün dosyayı tek seferde okur.
* readline : tek tek satırları okur. \n bakar.
* readlines() : bütün dosyayı okur ve liste yapısına kaydeder.

* yazma işlemini yapan metotlar :
* write() : \n yoktur. Bizim eklememiz gerekiyor.

* kapatma işlemi :
* close() :
--------
# pickle modul mevcut
* Herhangi bir nesneyi dosyaya kaydetmek için kullanılır.
* binary şeklinde kaydedilir.
"""

# ikinci parametre mode
# mode : yazma, okuma veya ekleme
# 'w' : write, 'r' : read, 'a' : append

# ogrenciler dosyası açıldı
dosya = open('ogrenciler',  'w')

# yazma işlemi
dosya.write("Eren\n")
dosya.write("Karadeniz\n")
dosya.write("CS\n")

# dosya kapatma işlemi
dosya.close()

### with ifadesi
	# dosyayı kapatmaya gerek kalmıyor.
with open("ogrenciler") as o:
	for line in o:
		print(line)

