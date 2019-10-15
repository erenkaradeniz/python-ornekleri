# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""
# Özellikleri(attribute) nelerdir ? fonksiyonlar ve tanımlanan değişkenler ** Sınav Sorusu

class Kare:
    """ Kareyi temsil eder. """
    #pass # herhangi bir işlem yapma anlamında
    nufus = 0
    
    def __init__(self, kenar = 1): # default değer atadık ama zorunlu değil.
        print("__init__ çalıştırıldı. ")
        self.kenar = kenar


    def cevre_hesapla(self):
        """ çevre hesaplar """
        return self.kenar * 4

    def alan_hesapla(self):
        """ alan hesaplar """
        return self.kenar ** 2

    def yazdir(self): # metodların içinde parametre olması gerek
        print("Ben bir kareyim.")

    def merhaba(self):
        print("")

    # override
    def __str__(self):
        """ sınıfın string karşılığı """
        return " r : %d alan : %d çevre : %d " % (self.kenar)

k1 = Kare() #__init__ fonksiyonu çalıştırılır.
print("Alan : ", k1.alan_hesapla())
print("Çevre : ", k1.cevre_hesapla())
k1.yazdir()