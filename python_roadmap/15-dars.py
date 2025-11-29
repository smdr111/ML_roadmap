# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:14:29 2023

@author: User
"""
# Lug`at elementlari bilan ishlash
# .items()metodi lug`at elementlari bn ishlaydi
gullar={
        'Rano':'paxta',
        'Barno':'lola',
        'Shahlo':'atirgul',
        'Maftuna':'boychechak'
        }
print(gullar.items())
# for bn
for a,b in gullar.items():
    print(f'Kalit:{a}')
    print(f'Qiymat:{b}\n')

gullar={
        'Rano':'paxta',
        'Barno':'lola',
        'Shahlo':'atirgul',
        'Maftuna':'boychechak'
        }
for key,val in gullar.items():
    print(f'{key.title()}ga {val}ni Sobir berdi.')

# .keys() metodi lug`at kaliti bn ishlaydi
taom={
      'Iskandar':'Manti',
      'Nazokat':'Osh',
      'Samandar':'Bosma',
      'Munisa':'Kebab',
      'Orifjon':'G`osht'
      }
print(taom.keys())
for k in taom.keys(): # keys() ishlatmasak ham bir hil natija chiqadi
    print(k.upper())
# Yuqoridagi kodimizda, for tsiklida .keys() metodini ishlatmasak ham huddi shu natija chiqadi.

gul=['Shahlo','apelsin','Maftuna','behi']
for g in gullar:
    if g in gul:print(f'{g}ga {gullar[g]} berishdi.')
    else:print(f'{g} bugun darsga kelmadi.')
    
# LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH.
# Pythonda lug'at elementlari siz 
# (foydalanuvchi) kiritgan tartibda saqlanadi. Agar lug'at elementlarini 
# alifbo bo'yicha chiqarish talab qilinsa, `sorted()` funktsiyasidan foydalanamiz.

for t in sorted(taom):
    print(t.lower())

# .values() metodi
print(sorted(taom.values()))

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
print(sorted(telefonlar.values()))
for v in telefonlar.values():
    print(v)

# SET funksiyasi
# Pythonda `set` yana bir ma'lumot turi bo'lib, ro'yxat va lug'at kabi bir 
# nechta elementlarni saqlashga mo'ljallangan. Lug'at va ro'yxatdan farqli ravishda, 
# `set` ichidagi elementlar biror tartibda saqlanmaydi, va ularga indeks orqali 
# murojat qilib bo'lmaydi. Shuningdek, set ichida bir hil elementlar bo'lmaydi.
print(set(telefonlar.values()))
for b in sorted(set(telefonlar.values())):
    print(b.upper())












