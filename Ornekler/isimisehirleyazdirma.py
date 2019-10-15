# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""

liste = { 
'a' : 'Ankara',
'b' : 'Bursa',
'c' : 'Ceyhan',
'd' : 'Denizli',
'e'	: 'Erzurum',
'f' : 'Fatsa',
'g' : 'Giresun',
'h' : 'Hatay',
'i' : 'İstanbul',
'j' : 'Jesolo',
'k' : 'Kastamonu',
'l' : 'Lüleburgaz',
'm' : 'Manisa',
'n' : 'Niğde',
'o' : 'Ordu',
'p' : 'Pamukkale',
'r' : 'Rize',
's' : 'Samsun',
't' : 'Trabzon',
'u' : 'Uşak',
'v' : 'Van',
'y' : 'Yozgat',
'z' : 'Zonguldak'
}


def girdi_al():
	girdi = input('isim giriniz : ')
	return girdi


def isim_donustur(karakterler):
	print('çıktı        :', end = ' ')
	for karakter in karakterler:
		if(karakter in liste):
			print(liste[karakter], end = ' ')


def main():
	karakterler = []
	girdi = girdi_al()
	girdi = girdi.lower()
	for i in girdi:
		if(i == 'ç'):
			karakterler.append('c')
		elif(i == 'ğ'):
			karakterler.append('g')
		elif(i == 'ı'):
			karakterler.append('i')
		elif(i == 'ö'):
			karakterler.append('o')
		elif(i == 'ş'):
			karakterler.append('s')
		elif(i == 'ü'):
			karakterler.append('u')
		else:
			karakterler.append(i)


	isim_donustur(karakterler)
	print()


main()