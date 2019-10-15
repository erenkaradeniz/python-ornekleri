# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""
class Silindir:
    """ Silindiri Temsil Eder. """
    pi = 3.14

    nufus = 0

    __sakli__ = 10

    def __init__(self, yaricap, yukseklik): # default değer atadık ama zorunlu değil.
        print("__init__ çalıştırıldı. ")
        self.yaricap = yaricap
        self.yukseklik = yukseklik
        Silindir.nufus += 1

    def hacim(self):
        """ hacim hesaplar """
        return Silindir.pi * (self.yaricap ** 2) * self.yukseklik

    def alan(self):
        """ alan hesaplar """
        return 2 * Silindir.pi * self.yaricap * (self.yaricap + self.yukseklik)

    def yazdir(self): # metodların içinde parametre olması gerek
        print("Ben bir silindirim.")
        print(Silindir.__sakli__)

    def nufus_yazdir(self):
        print("Nufus yazdir : ", Silindir.nufus)


sil1 = Silindir(2, 2) #__init__ fonksiyonu çalıştırılır.
sil2 = Silindir(3, 3)
print("Hacim : ", sil1.hacim())
print("Alan : ", sil1.alan())
sil1.yazdir()

# Erişim Fonksiyonları
print(hasattr(sil1, "yaricap"))
print(getattr(sil1, "yaricap"))
setattr(sil1, "yaricap", 5)
print(getattr(sil1, "yaricap"))
delattr(sil1, "yaricap")
print(hasattr(sil1, "yaricap"))

# Dahili (Built-in) alanlar.
print("sil1.dict", sil1.__dict__)
print("sil2.dict", sil2.__dict__)

print("sil1 name : ", Silindir.__name__)
print("sil1 doc : ", Silindir.__doc__)
print("sil1 modul : ", Silindir.__module__)