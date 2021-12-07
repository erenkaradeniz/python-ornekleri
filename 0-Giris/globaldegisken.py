# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""

"""
namespace: isim uzayı
scope : değişkenlerin etki alanı
local değişken : Fonksiyonların içinde tanımlanan değişkenlere yerel değişkenler denir. Yerel değişkenlere sadece içinde olduğu fonsiyonlardan erişilir.
global değişken : Tüm fonksiyonların dışında tanımlanan değişkenlere global değişkenler denir. Bu tür değişkenler tanımlandıktan sonraki her yerde kullanılabilir.
"""

def fonk():
    global d #global değişken tanımlama
    d = 43 # global değişkenler
    l = 21 # local değişkenler

def main():
    fonk()
    print("d: ", d)
    #print("l: ", l) NameError: name 'l' is not defined

main()
