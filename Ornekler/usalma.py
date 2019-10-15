# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""

def us_al(taban, us):
    """
    gönderilen sayının üssünü geri döndürür
    """
    return taban**us
    
def main():
    # 1. durum ile çağırma
    # 3^2
    print(us_al(3,2))

    # 2. durum ile çağırma
    # keyword passing
    print(us_al(us=2, taban=3))
    print(us_al(taban=3, us=2))

main()