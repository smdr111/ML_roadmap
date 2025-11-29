# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 00:48:04 2023

@author: User
"""

#1-masala
cars=['toyota','mazda','hyundai','gm','kia']
for car in cars:
        print(car.upper()) if car=="gm" else print(car.title())

# 2-masala
cars=['toyota','mazda','hyundai','gm','kia']
for car in cars:
        print(car.title()) if car!="gm" else print(car.upper())

# 3-masala
login=input('Login ismingizni kiriting:\n>>>')
if login.lower()=='admin':print('Xush kelibsiz, Admin. Foydalanuvchilar ro`yxatini ko`rasizmi?')
else:print(f'Xush kelibsiz,{login.title()}!')

# 4-masala
son1=input('Ikkita sonni kirting:\nBirinchi son:') 
son2=input('Ikkinchi son:')
if son1==son2:print('Sonlar teng!')
elif son1>son2:print('Birinchi son katta')
elif son1<son2:print('Ikkichi son katta')
#5-masala
number=int(input('Istalgan sonni kiriting:\n>>>'))
print('Manfiy son') if number<0 else print('Musbat son')

#6-masala
number=int(input('Istalgan butun sonni kirting:\n>>>'))
print(f'{number} ning kvadrat ildizi:{number**(1/2)}') if number>0 else print('Manfiy son,musbat son kiriting') 





