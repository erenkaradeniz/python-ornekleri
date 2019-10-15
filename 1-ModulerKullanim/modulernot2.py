# -*- coding: utf-8 -*-
#!/usr/bin/Python


"""
@author : Eren Karadeniz

Module :
* .py uzantılı her bir dosya bir modulü olmakta
* import keyword ile dahil ediliyor.
* üç tane dahil edilme yöntemi vardır.

1. import modulname --> en basit ve en kolay, namespace uygun bir yapısı var. 
	isim karmaşasını önler.

	modul1 - fonk1()
	modul2 - fonk1()

	modul1.fonk1()
	modul2.fonk1()

	import math as m --> takma isim tanımlaması yapılabiliyor.

2. from modulname import fonk1, fonk2, fonk3,...
	fonk1()

3. from modulname import * : _degisken : gizli değişkenlerdir dahil edilmiyor.
	fonk1()

built-in

* python modulleri sys.path de arıyor.
* '' ilk değişken boştur. Bu da bulunulan dizini temsil ediyor.

"""
# iki tane fonksiyon tanımlanacak
# ilkinde alt çizgi olacak diğerinde olmayacak

# dışarıya açık olan
def f(x):
	return x

# gizli fonksiyon
# _ alt çizgi özel tanımlamadır.
def _g(x):
	return x