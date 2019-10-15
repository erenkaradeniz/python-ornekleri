# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""
# Sınıf Kavramı
"""
class keyword ile tanımlanır.
genel yapısı

class sınıf_ismi:
	ifade1
	....
	ifadeN

	def fonksiyon_ismi:
		ifade1
		....
		ifadeN

o1 = sınıf_ismi() # nesne veya instance

* sınıflar birer plandır. blueprint
* instance : sınıfın bir örneği
* new keyword yok.
* attribute : özellik
* sınıf içerisindeki değişkenler veya fonksiyonlar
* sınıf içerisinde metot tanımlarken bir değişken tanımlanma gerekiyor. Bunun ismi de self olması tavsiye edilir.
Ancak self olmak zorunda değil.

# Kurucu metot (constructor)
* __init__(self) isminde bir kurucu metot vardır.
* amacı sınıfın alanlarına ilk değerlerini vermek.

# Erişim
* private, public, protected gibi değişkenler yok.
* "__" iki alt çizgi ile başlayan alanlar private olarak kabul edilir.
* iki alt çizgi ile bitmesi gerekmiyor.

# Erişim fonksiyonları
* getattr(obj, alan) : belirtilen alanın değerini döndürür.
* setattr(obj, alan, value) : belirtilen alanın değerini değiştirir.
* hasattr(obj, alan) : belirtilen alan var mı ? True: False
* delattr(obj, alan) : belirtilen alanı siliyor
* attr{get, set, del, has}
"""