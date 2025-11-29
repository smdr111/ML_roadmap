# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 22:29:17 2023

@author: User
"""

# Lug`at - Dictionary , ikki qismdan iborat: kalit so'z va izoh

gul_0={'lola':'red','paxta':'oq','archa':'yashil'}
print(gul_0['lola'])
print(gul_0['paxta'])

#Lug'atdagi qiymatlar son (int, float), matn (string), ro'yxat
#(list, tuple, set) va hatto boshqa lug'at ham bo'lishi mumkin.

malumot_0={'Ism':'Samandar','Familiya':'Oripov','Yosh':20,'t_yil':2003}
print(f"{malumot_0['Ism'].title()} {malumot_0['Familiya'].title()},\
{malumot_0['Yosh']} yoshda va {malumot_0['t_yil']}-yilda tug`ilgan.")

# Lug`atga yangi juftlik qo`shish
malumot_0['t_joy']='Uzbekistan'
malumot_0['otasi']='Iskandar'
malumot_0['singillari']=2
print(malumot_0)

# Bo`sh Lug`at
car_0={}
car_0['wheel']='rul'
car_0['lambo']='black'
car_0['ferrari']='red'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
car_0['mustang']='yellow'
print(car_0)
#Lug'atga kalit so'zlar qanday ketma-ketlikda kiritilsa, shu ketma-ketlik saqlanib qoladi.

#keyword-value juftligini o`chirish DEL
talaba_0={'Ism': 'Samandar', 'Familiya': 'Oripov', 'Yosh': 20, 't_yil': 2003,
          't_joy': 'Uzbekistan', 'otasi': 'Iskandar', 'singillari': 2}
print(talaba_0)
del talaba_0['singillari'],talaba_0['otasi'],talaba_0['t_joy']
print(talaba_0)

# LUG'ATNI QATORLARGA BO'LIB YOZISH\
gullar={
        'Rano':'paxta',
        'Barno':'lola',
        'Shahlo':'atirgul',
        'Maftuna':'boychechak'
        }
print(gullar)

# .get() METODI
gul=gullar['Rano']
print(f'Rano {gul} oldi')

gul=gullar.get('Odina','Bunday ism mavjud emas.')
print(gul)

# Agar `.get()` metodida ikkinchi argumentni tashlab ketsangiz, \
#va kalit mavjud bo'lmasa `.get()` metodi None degan qiymatni qaytaradi. 
#`None` - qiymat mavjud emas degan ma'noni beradi.

gul=gullar.get('Odina')
print(gul)



































