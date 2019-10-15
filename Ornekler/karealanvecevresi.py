# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""

def kare_alani(kenar):
    #docstring, pydoc
    """
    Karenin alanını hesaplar
    """
    return kenar**2 #kenar*kenar


def kare_cevresi(kenar):
    """
    Karenin çevresini hesaplar
    """
    return kenar*4


def main():
    kenar = 7
    alan = kare_alani(kenar)
    cevre = kare_cevresi(kenar)

    print("Karenin alani=", alan, "Karenin çevresi=", cevre)
    print("Karenin alani=", kare_alani(5), "Karenin çevresi=", kare_cevresi(5))
    print(kare_alani.__doc__)
    print(kare_cevresi.__doc__)



main()