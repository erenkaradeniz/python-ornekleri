# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""


import sys


def harflendirme(puan):
    if puan < 0 or puan > 100:
        print("Geçersiz giriş lütfen geçerli")
        main()
    elif puan < 40 :
        print("FF")
    elif puan < 50 :
        print("FD")
    elif puan < 55:
        print("DD")
    elif puan < 60:
        print("DC")
    elif puan < 65:
        print("CC")
    elif puan < 70:
        print("CB")
    elif puan < 75:
        print("BB")
    elif puan < 85:
        print("BA")
    elif puan <= 100:
        print("AA")
    main()


def main():
    try:
        puan = int(input("Notu giriniz veya çıkış için enter'a basınız : "))
    except ValueError:
        sys.exit("Çıkış Yapıldı")

    harflendirme(puan)


main()