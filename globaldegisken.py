# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""

"""
namespace: isim uzayı
scope : değişkenlerin etki alanı
local değişken :
global değişken :
"""

def fonk():
	global d #global değişken tanımlama
	d = 43 # global değişkenler
	l = 21 # local değişkenler

def main():
	print("d: ", d)


main()