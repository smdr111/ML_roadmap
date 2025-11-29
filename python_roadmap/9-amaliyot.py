# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 19:57:43 2023

@author: User
"""
# 1-masala
ismlar=['Abror','Nodir','Azim','Alish','G`ani']
for ism in ismlar:
    print(f'Bugun darsga {ism} kelmadi.')

# 2-masala
print('Kod 5 marta takrorlanadi')

# 3-masala
toq_sonlar=list(range(11,100,2))
for toq_sonlar_kubi in toq_sonlar:
    print(toq_sonlar_kubi**3)

# 4-masala
kinolar=[]
print("5 ta sevimli kinoyingiz qaysilar?")
for k in range(5):
    kinolar.append(input(f'{k+1}-kino:'))
print(kinolar)

# 5-masala
odamlar=[]
for odam in range(int(input('Bugun nechta odam bilan uchrashdingiz?'))):
    odamlar.append(input(f'{odam+1}-inson ismi:'))
print(odamlar)

davlatlar=[]
for d in range(int(input('Nechta chet el davlatlariga sayohat qilgansiz?'))):
    davlatlar.append(input(f'{d+1}-davlat nomi:'))
print(davlatlar)
    
    
    
    
    
    