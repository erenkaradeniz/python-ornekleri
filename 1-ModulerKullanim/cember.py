# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""
"""
Çember Alan ve Çevresi

* iki fonksiyon tanımlanacak
* alan ve cevre hesaplanacak
* pi sayısı global olarak tanımlanacak
* __name__ değişkeni : __main__
* __doc__ değişkeni
* standalone (main varmış gibi doğrudan çalıştırılıyor) 
* ve imported (kütüphane olarak kullanılan versiyon)
* pyc uzantılı dosyalar oluşturur.
* pycler derlenmiş bytecode içeren dosyalardır.
* amacı performans artırmaktır.
"""

# global değişken

pi = 3.14159

def alan(yaricap):
	""" Çemberin alanını hesaplar """
	return pi * yaricap * yaricap

def cevre(yaricap):
	""" Çemberin çevresini hesaplar """
	return 2 * pi * yaricap

# main kısmı
def main():
	print("r : 5 alanı : ",alan(5))
	print("r : 5 çevresi : ", cevre(5))

# standolne ve import çalıştırma belirlenecek

if __name__ == '__main__':
	# normal çalıştırma : python cember.py
	print("Normal program gibi çalıştırılıyor")
	print("isim : ",__name__)
	main()
else:
	# import ederek çalıştırma
	# cember
	print("isim : ", __name__)
	print("Kütüphane olarak dahil edilmiştir")