# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 01:48:44 2023

@author: User
"""

# 1-masala
davlatlar=['USA','UZB','UK','SIN','CANADA','RUSSIA','ALBANIA']
print(davlatlar)
print(len(davlatlar))#uznligi
print(sorted(davlatlar))# tartib
print(sorted(davlatlar,reverse=True))# Teskari tartib
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

# 2-masala
sonlar=list(range(120,1201,2))
print(sonlar)
print(sum(sonlar))
print(max(sonlar)-min(sonlar))
print(len(sonlar))
son1=sonlar[0:21]
son2=sonlar[500:521]
son3=sonlar[250:271]
print(son1)
print(son2)
print(son3)

#3-masala
taomlar=['osh','shorva','tuxum','Kabob','mastava']
nonushta=taomlar[:]
nonushta.remove('shorva')
del nonushta[3]
nonushta.append('coffe')
nonushta.insert(0,'butter')
print(nonushta)
print(taomlar)
nonushta=tuple(nonushta)
nonushta=list(nonushta)
nonushta[0]='qaymoq va saryog`'
nonushta=tuple(nonushta)
print(nonushta)
print(type(nonushta))















