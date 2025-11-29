# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:32:09 2023

@author: User
"""
# 1-masala
atamalar={'int':'butun son','float':'O`nlik son','title':'Bosh harf',\
       'str':'matn','upper':'hammasi katta harf','lower':'hammasi kichik harf',\
        'remove':'qiymat boyicha o`chiradi','del':'indeks bo`yicha o`chiradi',\
            'list':'ro`yxat','type':'o`zgaruvchi turini tekshirish'}
print(atamalar.values())
for v in atamalar.values():
    print(v)
for k,q in atamalar.items():
    print(f'Atama: {k}')
    print(f'Izoh: {q}\n')

telefonlar = {
        'ali':'iphone x',
        'vali':'galaxy s9',
        'olim':'mi 10 pro',
        'orif':'nokia 3310',
        'hamida':'galaxy s9',
        'maryam':'huawei p30',
        'tohir':'iphone x',
        'umar':'iphone x'    
        }
for a,b in telefonlar.items():
    print(f'Atama: {a}')
    print(f"Izoh: {b}\n")

# 2-masala
countries={'USA':'WASHINGTON','UZBEKISTAN':'TASHKENT','CANADA':'OTTAWA','SINGAPORE':'SINGAPORE',\
           'RUSSIA':'MOSKVA'}
for k,q in sorted(countries.items()):
    print(k)
    print(q)

# 3-masala
davlat=input('Istalgan davlatni kiriting:\n>>>')
if davlat in countries:
    print(f'{davlat.title()}nig poytaxti {countries[davlat]}.')
else: print('Bizda bunday ma`lumot yo`q.')

# 4-masala

taom={'osh':5000,'masatava':3000,'somsa':2500,'shashlik':6000,'manti':4000,\
      'lagmon':4500,'salad':2000,'choy':1500,'non':1000,'sho`rva':7000}
buyurtma=[]
print('Uchta ovqat buyurtma qiling!')
for b in range(3):
    buyurtma.append(input(f'{b+1} ovqat nomi:'))
for k in buyurtma:
       if k.lower() in taom:print(f"{k.title()} narxi {taom[k]} so`m.")
       else:print(f" Bizda {k.upper()} yo`q")



































