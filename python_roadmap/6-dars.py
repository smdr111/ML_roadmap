# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 01:45:25 2023

@author: Samandar
"""
# INTEGERS - Butun sonlar(int)

a=23
b=-15
c=a+b
print(c)
kvdrt_tmni=12
kvdrt_yuzi=kvdrt_tmni**2
print(kvdrt_yuzi)

# FLOATS - O`nlik sonlar (float)

pi=3.14159
radius=10
doira_yuzi=pi*radius**2
print('doiraniong yuzi ', doira_yuzi,' ga teng.')

# Butun va o`nlik son
d=36
f=3
e=(d/f)
print(e)
print(d//f) # // sonning butun qismini olish
a=5
b=8.0
print(a+b) 
print(a-b) 
print(a*b)
print(a/b)
print(a**b)

# Uzun sonlar
odam_soni=7_879_000_000 # pastki chiziq bo`lsa ham son deb oladi.
print('Yer yuzida ',odam_soni,' inson mavjud.')

#Konstanta
PI=3.141593# konstanta odatda katta harfda yoziladi.
radius=21.2

# Birdan ortiq o`zgaruvchilarga qiymat berish
x,y,z=10,16,36

# O`zgaruvchi turini almashtirish
ism='Jobir'
yosh=36
xabar=ism+' '+str(yosh)+' yoshda'
print(xabar)

# str()= int yoki float ko`rinishidagi sonlarni matnga aylantiradi
# int()= float yoki str ni butun songa aylantiradi. Matn butun bo`lishi kerak
# float()= str yoki int ni o`lik songa aylantiradi

# O`zgaruvchi turini tekshirish TYPE() orqali
ism='Jobir'
yosh=36
print(type(ism))
print(type(yosh))

# INPUT VA SONLAR
t_yil=int(input('Tug`ilgan yilingiz?'))
yosh=2023-t_yil
print('Siz '+str(yosh)+' yoshda ekansiz.')


































