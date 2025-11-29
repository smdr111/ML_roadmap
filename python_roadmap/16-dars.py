# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 05:40:30 2023

@author: User
"""
# NESTING
#Ba'zida dasturlash jarayonida lug'atning ichida ro'yxatlar yoki boshqa lug'atni, 
#yoki aksincha ro'yxat ichida lug'atni saqlash ham qo'l kelishi mumkin. Bu ingliz 
#tilida Nesting deyiladi.
car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
        }
cars=[car1,car2,car0]
for car in cars:
    print(f'{car["model"].title()},{car["rang"]} rangda,{car["yil"]} yil,{car["narh"]} so`m')
print(cars[0])
print(cars[1]["km"])

malumot=[]
for m in range(10):
    talaba={
        'Ismi':"Javlon",
        'Yoshi': None,
        'Familiyasi':None,
        'T_joyi':'Fergana',
        'Millati': None
        }
    malumot.append(talaba)
print(malumot)

for mal in malumot[:4]:
    mal['Yoshi']=18
for mal in malumot[4:9]:
    mal['Yoshi']=21
for mal in malumot[9:]:
    mal['Yoshi']=23
for mal in malumot[:5]:
    mal['Familiyasi']='Nabiyev'
for mal in malumot[5:]:
    mal['Familiyasi']='Aliyev'
for mal in malumot:
    if mal['Yoshi']==18:
        mal['Millati']='Uzbek'
    if mal['Yoshi']==21:
        mal['Millati']='Russian'
    if mal['Yoshi']==23:
        mal['Millati']='American'
for mal in malumot:
    print(malumot)

# LUGAT ICHIDA RO`YXAT

dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())
# boshqa usuli
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
    for til in tillar:
        print(f'{til.upper()} ', end='')
        
# LUG`AT ICHIDAGI LUG`AT

hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
             }
for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:", end='')
    for til in info['tillar']:
        print(til.upper(), end='')



















































