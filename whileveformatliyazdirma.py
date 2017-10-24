# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz


Formatlı yazdırma ve while yapısı
	# d : decimal : tam sayı
	# f : float : reel sayı
"""

i = 0

sayac = 0

while i < 1:
	print('{:2d} {:3f}'.format(sayac, i))
	i = i + 0.1
	sayac = sayac + 1
	#else yapısı kullanılabilir zorunlu değil
else:
	print("Döngü bitti")