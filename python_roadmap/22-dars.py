#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 11:56:33 2025

@author: samandaroripov
"""
# Funksiya so`ngi so`z

# lambda nomsiz funksiya
# lambda argument:ifoda

import math
uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,10))


product = lambda x, y : x ** y
print(product(3, 2))

def daraja(n):
    return lambda x : x**n

kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")

# map() funksiyasi

from math import sqrt

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
ildizlar = list(map(sqrt,sonlar))
print(ildizlar)

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati

def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x*x

print(list(map(daraja2,sonlar))) # sonlar ning kvadratini hisoblaymiz

print(list(map(lambda x:x*x,sonlar)))


a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x,y:x+y,a,b))
print(a_plus_b)

a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x,y:x+y,a,b))
print(a_plus_b)

# filter() funksiyasi

import random as r

sonlar=r.sample(range(1,100),10)
juft_sonlar=list(filter(lambda x:x%2==0,sonlar))
print(juft_sonlar)


mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

print(list(filter(lambda a:a.startswith('o'),mevalar)))

mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar2)

# .startswith(), .endswith()































