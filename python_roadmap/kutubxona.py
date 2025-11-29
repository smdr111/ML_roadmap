#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 11 12:16:27 2025

@author: samandaroripov
"""

# pyhtom standard kutubxonasi

# datetime_ Sana va vaqt
import datetime as dt
hozir = dt.datetime.now()
print(hozir)

# sanani ajratib olish
print(hozir.date())

# vaqtni ajratib olish
print(hozir.time())

# soatni ajratib olish
print(hozir.hour)

# minutni ajratib olish
print(hozir.minute)

# sekundni ajratib olish
print(hozir.second)

bugun = dt.date.today()
print(f"Bugungi sana: {bugun}")

ertaga = dt.date(2021, 6, 21)
print(f"Ertangi sana: {ertaga}")

hozir = dt.datetime.now()
vaqtHozir = hozir.time()
print(f"Hozir soat: {vaqtHozir}")

# Istalgan vaqtni qoʻlda kiritish uchun esa `.time()` metodiga 
# kerakli vaqtni (soat, minut, sekund) koʻrinishida beramiz:
vaqtKeyin = dt.time(23,45,00)


# Ayirish operatori yordamida sanalalar va vaqtlar orasidagi 
# farqni hisoblashimiz mumkin:
bugun = dt.date.today()
qurbonHayit = dt.date(2021, 7, 19)
farq = qurbonHayit-bugun
print(farq)
print(f"Qurbon Hayitiga {farq.days} kun qoldi")

# Huddi shu kabi ikki vaqt oraligʻini sekundlarda 
# yoki soatlarda ham koʻrishimiz mumkin:

hozir = dt.datetime.now()
futbol = dt.datetime(2021, 6, 22, 23, 45, 00)
farq= futbol-hozir
sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(f"Futbol boshlanishiga {sekundlar} sekund qoldi")
print(f"Futbol boshlanishiga {minutlar} minut qoldi")
print(f"Futbol boshlanishiga {soatlar} soat qoldi")

# Yuqorida sanalar AQSh standartiga koʻra, yil-oy-kun koʻrinishida chiqayapti. 
# Sanani oʻzimizga moslab chiqarish uchun `.strftime()` metodini chaqiramiz, 
# va sanani oʻzimizga qulay formatda chiqaramiz.
# vaqtni millisekundsiz chiqaramiz
vaqt = hozir.strftime("%H:%M:%S")
print(f"Hozir soat: {vaqt}") 

# sanani kun-oy-yil koʻrinishida chiqaramiz
sana = hozir.strftime("%d-%m-%Y")
print(f"Bugun sana: {sana}")

# sanani kun/oy/yil koʻrinishida chiqaramiz
sana_vaqt = hozir.strftime("%d/%m/%Y, %H:%M")
print(sana_vaqt)

# math - Matematik funksiyalar
#  SONLARNI YAXLITLASH

# Sonlarni eng yaxlitlash uchun Pythonda maxsus `round()` funksiyasi mavjud. 
# Bunga qo'shimcha ravishda, `math` moduli ichidagi `ceil()` funksiyasi yordamida berilgan o'nlik 
# sonni keyingi butun songa, `floor()` yordamida esa quyi butun songa yaqinlashtirish mumkin:
import math

x = 4.6
print(math.ceil(x))

print(math.floor(x))

print(round(x))

x = 81

# Kvadrat ildiz
math.sqrt(x)

# Darajaga oshirish
math.pow(x,3) # x ning kubi

# `pprint` - CHIROYLI PRINT

# `pprint` moduli yordamida turli o'zgaruvchilarni chiroyli ko'rinishda 
# konsolga chiqarishimiz mumkin. Bu bizga uzun lug'atlar, JSON fayllar yoki 
# matnlar bilan ishlashda juda asqotadi.


dori={'allergiya': None,
 'dorilar': [{'miqdori': 0.5, 'nomi': 'Analgin'},
             {'miqdori': 1.2, 'nomi': 'Panadol'}],
 'farzandlar': ['Ahmad', 'Bonu'],
 'ism': 'Alijon Valiyev',
 'oila': True,
 'yosh': 30}
from pprint import pprint
print(dori)
pprint(dori)

# Regex - Andoza yordamida matn izlash 
import re
with open('words.txt','r') as file:
       word_list=[line.strip() for line in file]

andoza='^t...e$'
matches=[]
for word in word_list:
    if re.match(andoza,word):
        matches.append(word)
print(matches)    

# Andozalar biror matnda biz uchun kerakli maʻlumotlarni ajratib olish uchun juda qulay. 
# Masalan, Telegram orqali yuborilgan habardan email manzilini yoki telefon raqamini 
# ajratib olish uchun maxsus andoza yozishmiz mumkin. 
# [ihateregex.io](https://ihateregex.io) sahifasidan 
# esa loyihangiz uchun tayyor andozalarni topishingiz mumkin. 
















































