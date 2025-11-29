#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 00:27:56 2025

@author: samandaroripov
"""
# FUNKSIYA
# DOCSTRING
# print(funksiya_nomi.__doc__)

def toliq_malumot(ism,familiya,yil):
    'Foydalanuvchining ismi familiyasi va yoshini chiqaruvchi funksiya'
    print(f'Ismi:{ism.title()}\n'
          f'Familiyasi:{familiya.title()}\n'
          f'Tugilgan yili:{2025-yil}')

ism1=input('Ismingizni kiriting: ')
familiya1=input('Familiyangizni kiriting: ')
yil1=int(input('Yoshingizni kiriting: '))
toliq_malumot(ism1,familiya1,yil1)

def hisobla(son):
    'Sonning kvadrati va kubini hisoblovchi funksiya'
    print(f'Sonning kvadrati: {son**2}\n'
          f'Sonning kubi: {son**3}')
son1=float(input('Istalgan son kiriting: '))
hisobla(son1)


def aniqla(son):
    'Sonning juft yoki toqligini aniqlovchi funksiya'
    if son%2==0:print('Juft son')
    else:print('Toq son')
    
son2=float(input('Istalgan musbat son kiriting: '))
aniqla(son2)


def taqqosla(a,b):
    'Ikkita sonni taqqoslovchi funksiya'
    if a>b:print(f'{a}>{b}')
    elif a<b:print(f'{a}<{b}')
    else: print(f'{a}={b}')

x=float(input('Istalgan 2 ta son kiriting.\n1-son: '))
y=float(input('2-son: '))
taqqosla(x,y)

def kopaytir(x,y):
    '2-argumentni daraja shaklida hisoblaydigan funksiya'
    print(f'{x }ning {y}-chi darajasi: {x**y}')

x=float(input('Istalgan 2 ta son kiriting.\n1-son: '))
y=float(input('2-son: '))
kopaytir(x,y)


def kopaytir(x,y=2):
    '2-argumentni daraja shaklida hisoblaydigan funksiya'
    print(f'{x }ning {y}-chi darajasi: {x**y}')

x=float(input('Istalgan 2 ta son kiriting.\n1-son: '))
y=float(input('2-son: '))
kopaytir(x,y)


def divide(x):
    "Sonni 2 dan 10 gacha sonlarga qoldiqsiz bo`linishini tekshirish"
    for n in range(2,11):
        if x%n==0:print(f'{x} {n} ga qoldiqsiz bo`linadi')

y=float(input('Istalgan musbat son kiriting: '))
divide(y)













