# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""

"""
Üç tane veri yapısı (değişken) var.
list(liste), 
dictionary(sözlük),
tuple(tüp).

#list = []
kare parantez kullanılır değerler deiştirilebiliyor
(mutable)

# dictionary = {}
küme parantezi kullanılır ve ikili değerler kullanılır
{pencil: "kalem", door: "kapı"} integer da olabilir
anahtar değer ilişkisi vardır
değerler değişebilir (mutable)

# tuple = ()
parantez kullanır
değerleri değiştirilemez (immutable)
"""

liste = ["Eren"]
liste.append("Karadeniz")
liste.append("201313172085")
liste.append(5)
print(liste)

liste = [i**2 for i in range(1, 10)] # [1, 4, 9, 16, 25, 36, 49, 64, 81]

print(liste)

print(liste[-1]) #son elemanı

len(liste)

listebos = []


liste1 = list("eren") #['E', 'r', 'e', 'n']

liste1.count("e") # 2
liste1.index('r') # 1

print("n" in liste1) # true // "m" not in liste1 #true


liste2 = [i for i in range(0, 100)]

print([i for i in range(0, 100)])

#slicing

liste2[40:60] # 40-60 arası

liste2[40:60:5] # 40-60 arası 5'er artarak

liste2[-1] # Son eleman

liste2[-2:] # Son iki eleman

liste[:-2] # Son iki eleman hariç diğerleri

liste2[-1]

liste2[-4::2] # -4ten başlıyor 2şer 2şer

liste2.insert(2, 99)

liste2.sort()

rakamlar = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
rakam = (0,) # Tek eleman olunca virgül zorunlu

s = "Eren", 22, "CS" # Tuple packing
name, age, major = s # Tuple unpacking

d1 = {}
d2 = dict() # both empty
d3 = {"Name" : "Eren", "Age" : 22, "Major" : "CS"}
d4 = dict(Name = "Eren", Age = 19, Major = "CS")
d5 = dict(zip(['Name', 'Age', 'Major'], ['Eren', 22, 'CS']))

listd1 = [0, 1]
listd2 = ["False", "True"]
d6 = dict(zip(listd1, listd2))

d6[0]
print(d6)

del d6[0] # 0 keyi value ile siliniyor

d6.clear() # Tüm dictinoary siliniyor ve boş kalıyor

d6 = dict(zip(listd1, listd2))

d6.values()

#listedd = list(d6.values)