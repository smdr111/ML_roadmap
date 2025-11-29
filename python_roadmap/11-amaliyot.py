# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 06:00:22 2023

@author: User
"""

# 1-masala
son=int(input('Juft son kiriting:\n>>>'))
json=range(2,100000,2)
if son in json:print('Rahmat!')
else:print('Kechirasiz bu toq son.')

# 2-masala
yosh=int(input('Yoshingizni kiriting:\n'))
if yosh<=4 or yosh>=60:print('Sizga kirish bepul')
elif yosh>=18:print('Sizga kirish 20000 so`m.')
elif yosh<18:print('Sizga kirish 10000 so`m.')

# 3-masala
a=int(input('Istalgan 2 ta sonni kiriting!\nBirnichi son:'))
b=int(input('Ikkinchi son:'))
if a>b:print('Birinchi son katta')
elif a==b:print('Ikkala son teng')
else:print('Ikkinchi son katta')

#4-masala
mahsulotlar=['tarvuz','qovun','olma','banan','olcha','behi','sabzi','guruch','gilos','ko`kat']

son=int(input('Nechta mahsulot sotib olmoqchisiz:\n>>>'))

savat=[]
for n in range(son):
    savat.append(input(f"{n+1}-mahsulotni qo`shing:")) 

if savat:
    for xarid in savat:
        if xarid in mahsulotlar:print(f'Do`konimizda {xarid} bor.')
        else:print(f'Do`konimizda {xarid} yoq.')
else:print('Uzr savatingiz bo`sh')

# 5-masala
mahsulotlar=['tarvuz','qovun','olma','banan','olcha','behi','sabzi','guruch','gilos','ko`kat']

savat=[]
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni qo`shing:")) 
bor_mahsulotlar=[]
mavjud_emas=[]
for xarid in savat:
     if xarid in mahsulotlar:bor_mahsulotlar.append(xarid)
     else:mavjud_emas.append(xarid)
     
if mavjud_emas:
    for xarid in mavjud_emas:
        print(f'Kechirasiz bizda {xarid} yo`q')
else:print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# 6-masala,
users=['sam','tom','sean','nick','evan']
login=input('Login yarating:\n')
if login in users:print("Login band, yangi login tanlang!" )
else:print('Xush kelibsiz!')

#7-masala
son=int(input('Istalgan butun sonni kirting:\n'))
a=range(2,11)
for n in a:
    if not son%n:print(n)
   


























