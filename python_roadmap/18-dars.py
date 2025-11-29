#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 02:07:43 2025

@author: samandaroripov
"""
# QIYMAT QAYTARUVCHI FUNKSIYA

def full_info(name,surname,country,year,email='',number=None):
    fullinfo={'Ismi':name,
              'Familiyasi':surname,
              'T_joy':country,
              'T_yil':year,
              'email':email,
              'number':number
              }
    return fullinfo
print('Mijozlar ma`lumotini kiriting: ')
mijozlar=[]
while True:
    ismi=input('Ismi: ')
    familiyasi=input('Familiyasi: ')
    t_joy=input('Tug`ilgan mamlakati: ')
    t_yil=int(input('Tug`ilgan yili: '))
    email=input('E-mail address: ')
    number=int(input('Telefon raqami: '))
    mijozlar.append(full_info(ismi,familiyasi,t_joy,t_yil,email,number))
    savol=input('Yana ma`lumot kiritasizmi (ha/y`oq): ')
    if savol=='ha':
        continue
    else:
        break
    
for mijoz in mijozlar:
    print(mijoz)

def kattasi(x,y,z):
    max = x
    if y>=max:
        max = y
    if z>=max:
        max = z
    return max

kattasi(10,20,-5)


def aylana_info(r,p=''):
    info={'Radius':r,
          'Diametr':2*r,
          'Uzunligi':2*p*r,
          'Yuzi':p*(r**2)}
    return info

def tub_sonlar_top(min,max):    
    tub_sonlar = []    
    for n in range(min,max+1):
        tub = True
        if (n==1):
            tub = False
        elif(n==2):
            tub = True
        else:
            for x in range(2,n):
                if(n%x==0):
                    tub = False
        if tub:
            tub_sonlar.append(n)
                
    return tub_sonlar

tub_sonlar_top(1,20)

def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)        
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

print(fibonacci(10))















