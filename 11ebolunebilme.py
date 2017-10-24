# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
1-100000 11'e bölünebilme
"""


def bolunebilme(a):
	b = []
	for sayi in a:
		if(sayi % 11 == 0):
			b.append(sayi)

	return b

def main():
	liste = []

	for i in range(1,100001):
		liste.append(i)

	print(bolunebilme(liste))


main()