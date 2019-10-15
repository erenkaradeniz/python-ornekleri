# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""
"""
Exceptions
istisnalar
gerçersiz kod parçalarını yönetmeyi sağlar
ZeroDivisionError : sıfıra bölme hatası
try-except blokları içine alınır.
genel yapısı
try: # kodun denendiği kısım
	statement
except: # hata meydana gelirse, icra edilen kısım
	statement
# Hata Türleri
# SyntaxError : grammer yapısı hataları gibi
# ZeroDivisionError : 0'a bölme hatası
# TypeError  "23" + 45
# IOError : giriş çıkış hatası
# NameError : bulunmayan değişkene erişim hatası name 'a' is not defined 
# IndexError : bulunmayan indexe erişim hatası list index out of range

# Hata yakalama elemanları
## except
#zorunlu elemanlar
# hata meydana geldiğinde çalıştırılır

except:
	* tüm hata türleri için devreye girer.

except name:
	* tek bir hata türü

except name as n:
	* takma isim kullanılabilir.
	* tek bir tür için

except (name1, name2,...):
	* birden fazla hata için kullanılır.

except (name1, name2,...) as m:
	* takma isim kullanılır.	

## try:
# zorunlu eleman
# hata meydana gelebilecek yer tutulur

## else:
# opsiyonel
# hata meeydana gelmediği durumlarda kullanılır

## finally:
# opsiyonel
# hata meydana gelse de gelmese de çalıştırılır.

## raise:
	* manual olarak hata fırlatmayı sağlar.

## assert ifadesi
* birim test kullanılır.
assert ifade

a = 2
assert a == 2

"""

a = int(input("ilk sayıyı giriniz"))
b = int(input("ikinci sayıyı giriniz"))

print("Sonuc : ", a/b)


