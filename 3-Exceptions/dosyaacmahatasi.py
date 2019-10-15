# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""

"""
* Bulunan dizindeki bir dosyayı açmaya çalışalım.
* dosya dizinde mevcut olmadığı durumu
"""

dosya_adi = "takimlar"

try:
    dosya = open(dosya_adi, "r")
except FileNotFoundError:
    print("Dosya bulunamadı")

try:
    print(dosya.read())
    dosya.close()
except NameError:
    print:("Dosya mevcut değil")


dosya_adi2 = "takimlar2"

try:
    dosya = open(dosya_adi2, "r")
    print(dosya.read())
    dosya.close()
except:
    print("Dosya bulunamadı")
else:
    print("Kod hatasız çalıştı!")
finally:
    print("Hata olsa da olmasa da çalışacak")