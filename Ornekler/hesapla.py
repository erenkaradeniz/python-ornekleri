# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""

import math as m

def girdi_al():
    girdi = int(input(" giriniz : "))
    return girdi

def karekok(sayi):
    return m.sqrt(sayi)

def kare(sayi):
    return sayi**2

def hipo_bul(sayi1, sayi2):
    return karekok(kare(sayi1) + kare(sayi2))

def topla(sayi1, sayi2):
    return sayi1 + sayi2

def main():
    print(hipo_bul(girdi_al(), girdi_al()))

main()