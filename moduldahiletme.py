# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""


# iki kenarı alıp hipotenüsünü hesaplayan fonksiyon
# fonksiyonu bir değişkene atanması
# math modülü kullanımı
# modul dahil etmek için import kullanılır

import math


def hipo_bul(a, b):
	"""
	a^ + b^ = c^2
	"""
	return math.sqrt(a**2 + b**2)

def main():
	print(hipo_bul(3,4))

	# fonksiyonlar da bir nesnedir ve değişken isimleri değiştirilebilir

	# hipo_bul başka bir değişkene atandı
	yeni_hipo = hipo_bul

	print(yeni_hipo(5,12))
	

main()