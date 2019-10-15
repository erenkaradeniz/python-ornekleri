# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""
"""
# Miras alma
* Çoklu mirasa destek veriyor
* class sınıf_ismi(ust sınıf ismi)
* class sınıf_ismi(ust1, ust2, ...)
"""

# Kisi sınıfı
# Ogrenci(Kisi) Sınıfı
# Ogretmen(Kisi) Sınıfı

class Kisi:
	""" Kişiyi temsil eden sınıftır. """
	def __init__(self, isim, yas):
		self.isim = isim
		self.yas = yas

	def listele(self):
		print("isim : ", self.isim, " yas : ", self.yas)

class Ogrenci(Kisi):
	def __init__(self, isim, yas, numara):
		# Üst sınıfa bilgiler gönderiliyor.
		Kisi.__init__(self, isim, yas)
		self.numara = numara

	def listele(self):
		# isim ve yas kısımlarının yazdırılması
		Kisi.listele(self)
		print("numara : ", self.numara)

class Ogretmen(Kisi):
	def __init__(self, isim, yas, brans):
		# üst sınıfın kurucu metodunu çağırılıyor
		Kisi.__init__(self, isim, yas)
		self.brans = brans

	def listele(self):
		Kisi.listele(self)
		print("brans : ", self.brans)

o1 = Ogrenci("Eren", "22", 2013)
k = Ogretmen("Gürcan", "33", "Bilgisayar")

o1.listele()
k.listele()