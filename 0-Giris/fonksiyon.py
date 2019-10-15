# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""


def hello_func(name, somelist):
    print("Hello,", name, "!\n")
    name = "Caitlin"
    somelist[0] = 3
    return 1, 2


myname = "Ben"
mylist = [1, 2]
a, b = hello_func(myname, mylist)
print(myname, mylist)
print(a, b)

#String parametre olarak giderken listeler adres olarak gider. Tuple kopya olarak gider

def fonk1():
    print("parametresiz")


def fonk2(name):
    print("Merhaba", name)

def kare(a):
    return a*a

def fonk4(name, address = "Kütahya"):
    print(name, address)

fonk1()
fonk2("Eren")
print(kare(5))

fonk4("Eren", "Samsun")
fonk4("Eren")

def f(x):
    return x**2

print(f(8))

g = lambda x: x**2
print(g(8))