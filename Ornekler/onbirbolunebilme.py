# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""

def main():
    sayilar = [i for i in range(100000)] # Sayı dizisi oluşturma

    for sayi in sayilar:
        if(sayi % 11 == 0):
            print('{:3d} {:10d}'.format(sayi, sayi))

main()