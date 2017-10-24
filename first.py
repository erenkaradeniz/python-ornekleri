# -*- coding: utf-8 -*-
#!/usr/bin/Python


"""
@author : Eren Karadeniz
çoklu yorum satırları
pydoc
"""

i, j=2, 3

#print(i*j)

def fib(a):
    if a == 0:
        return 0
    if a == 1: 
        return 1
    return fib(a-1)+fib(a-2)
#print(fib(50))

puan = 55

if puan < 50:
    print("Kaldı")
elif puan < 80 and puan > 50:
    print("Geçti")
else:
    print("Wow")

# || = or, && = and
"""
ödev:
notun harf aralıklarını belirleyen (AA, BA, .... FD, FF) uygulama
Kullanıcıdan girdi alsın
Sadece .py uzantılı dosya
"""