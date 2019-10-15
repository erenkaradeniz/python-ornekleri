# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""

#operator overloading

class Kesir:
    def __init__(self, pay, payda):
        self.pay = pay
        self.payda = payda

    def __str__(self):
        return str(self.pay) + " / " + str(self.payda)

    def __add__(self, other):
        yeni_pay = (self.pay * other.payda) + (self.payda * other.pay)
        yeni_payda = self.payda * other.payda
        return Kesir(yeni_pay, yeni_payda)

    def __sub__(self, other):
        yeni_pay = (self.pay * other.payda) - (self.payda * other.pay)
        yeni_payda = self.payda * other.payda

        return Kesir(yeni_pay, yeni_payda)

    def __mul__(self, other):
        yeni_pay = self.pay * other.pay
        yeni_payda = self.payda* other.payda

        return Kesir(yeni_pay, yeni_payda)

    def __truediv__(self, other):
        yeni_pay = self.pay * other.payda
        yeni_payda = self.payda * other.pay

        return Kesir(yeni_pay, yeni_payda)

    def __lt__(self, other):
        """ > """
        value_a = (self.pay / self.payda)
        value_b = (other.pay / other.payda)

        if value_a > value_b:
            return True
        else:
            return False


a = Kesir(1, 2)
b = Kesir(3, 4)

c = a + b

print(a, " + ", b, "= ", c)

c = a - b

print(a, " - ", b, "= ", c)

c = a * b

print(a, " * ", b, "= ", c)

c = a / b

print(a, " / ", b, "= ", c)

c = a < b

print(a, " > ", b, "= ", c)