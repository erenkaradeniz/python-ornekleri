# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""

# üç tane fonksiyon tanımlanacak
# kendisine gün değeri gönderilecek ve saniye, dakika, saat değeri hesaplanacak
# üç fonksiyon dictionary de tutulacak
# çağrımları yapılacak

def gun_to_saat(gun):
    """
    Kendisine gönderile gün değerinin saat karşılığını hesaplar
    """
    return gun * 24

def gun_to_dakika(gun):
    """
    Kendisinie gönderilen gün değerinin dakika karşılığını hesaplar
    """
    return gun_to_saat(gun) * 60

def gun_to_saniye(gun):
    """
    Kendisine gönderilen gün değerinin saniye karşılığını hesaplar
    """
    return gun_to_dakika(gun) * 60


def main():
    # 1. Durum
    print("Saat:",gun_to_saat(20))
    print("Dakika:",gun_to_dakika(20))
    print("Saniye:",gun_to_saniye(20))
    
    # 2. Durum
    # dictionary yapısında tutulması
    # fonksiyonlar birer nesnedir!!!

    fonksiyonlar = {
     'gToSt' : gun_to_saat,
     'gToDk' : gun_to_dakika,
     'gToSn' : gun_to_saniye
     }

    print("20 gün ", fonksiyonlar['gToSt'](20))

    for f in fonksiyonlar:
        print("5 gün  ", fonksiyonlar[f](5))

    # lambda bir operator
    # isimsiz fonsiyonlar oluşturmayı sağlar
    # lambda param1, param2, .... : ifade

    fonksiyonlar2 = {
    'gToSt' : lambda gun: gun * 24,
    'gToDk' : lambda gun: gun * 24 * 60,
    'gToSn' : lambda gun: gun * 24 * 60 * 60
    }

    for f in fonksiyonlar2:
        print("10 gün  ", fonksiyonlar[f](10))

main()