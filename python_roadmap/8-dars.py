# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 00:03:41 2023

@author: User
"""

# Ro`yxat ichidagi elementlarni alifbi tartibida tartibash .SORT() METODI  orqali

cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort()
print(cars)
# > **Diqqat!** Tartiblashda katta harflar kichik harflardan avval kelishini 
#hisobga oling. Agar matndagi so'zlarning bosh harfi katta-kichik aralash yozilgan 
#bo'lsa, ularni bir ko'rinishga keltirib olish maqsadga muvofiq bo'ladi.
cars = ['Bmw','mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
cars.sort()
print(cars)
# Ro`yxat ichidagi elementlarni teskari alifbo tartiblash .sort(reverse=TRUE)
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort(reverse=True)
print(cars)
# .sort() bu tartiblash metodi, SORTED() FUNKSIYASI esa asl ro`yxatni o`zgartirmay tartiblaydi
mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)
# `sorted()` funktsiyasi yordamida teskari tartiblash uchun ham `reverse=True` argumentini beramiz
print(sorted(mehmonlar, reverse=True))

# Ro`yxatni almashtirish (boshini oxiriga, oxirini boshiga) . REVERSE() metodi
gullar=['lola','paxta','guncha','atir']
gullar.reverse()
print(gullar)

# Ro`yxat uznuligi LEN() funksiyasi

ismlar=['ali','vali','gani','obid']
print('Bugun darsga',len(ismlar),'dona oq`uvchi keldi')
print(ismlar)

# RANGE() funksiyasi

sonlar=list(range(0,9)) # range() 0 dan 9 gacha sonlarni shakllaydi list() esa ro`yxatga aylantiradi 
print(sonlar) # range funksiyasi har doim 2-indeksdan oldin to`xtaydi

# range() orqali qadamni ham berishimiz mumkin
juft_sonlar=list(range(0,20,2))
toq_sonlar=list(range(1,20,2))
print('Juft sonlar:',juft_sonlar)
print('Toq sonlar:', toq_sonlar)
# Agar range() 1-indeks 0 bolsa uni yozish shart emas
sonlar1=list(range(14))
print(sonlar1)

# Sonlar ustida sodda amallar MIN(), MAX(), SUM() funksiyalari

sonlar2=[155,898,321,9784,2350,6589]# BU NARHLAR ROYXATI BOLSIN
eng_arzon=min(sonlar2)
eng_qimmat=max(sonlar2)
jami_narh=sum(sonlar2)
print('Eng arzon paypoq', eng_arzon,'eng qimmat paypoq',eng_qimmat,'Jami',jami_narh)
 
# Ro`yxatni kesish []

cars=['bmw','nexia','damas','lambo','mers','ferrrari']
uzbek_cars=cars[0:4] # 2-indekssan 1 ta oldingisini tanlaydi
print(uzbek_cars)
# boshlangich indeks berilmasa royxat boshidan,oxirgi indeks berilmasa royxat oxirigacha kesadi

# Agar ikkala indeks ham berilmasa NUSXA oladi [:]

sonlar3=[48,56,78,98,20,155,15,51,1548]
raqam=sonlar3[:]
raqam.append(987)
raqam.append(654)
print(raqam)
print(sonlar3)

# O'zgarmas ro`yxat TUPLE() funksiyasi
toys=('bear','wolf','lion','Dolly')
# tuple elementlariga ham [] bilan murojaat qilinadi
#ys.append("dog")
print(toys) # no  changes
# tuple() funksiyasini o`zgartirish uchun list() funksiyasiga o`zgartiriladi
toys=list(toys)
toys.append('dog')
toys.remove('Dolly')
toys.insert(0,'cat')
toys=tuple(toys)
print(toys)

























