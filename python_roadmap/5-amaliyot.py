# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 06:04:57 2023

@author: User
"""

kocha='Bog`bon'
mahalla='Sag`bon'
tuman='Bodomzor'
viloyat='Samarqand'
print(kocha+' kochasi,',mahalla+' mahallasi,',tuman+' tumani,',viloyat+' viloyat.')
print(kocha+' kochasi,\n',mahalla+' mahallasi,\n',tuman+' tumani,\n',viloyat+' viloyat.')

manzil=f'{kocha} {mahalla} {tuman} {viloyat}'
print(manzil)

print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())

print('Iltimos quyidagi ma`lumotlarni kiriting:')
kocha=input('Ko`changiz nima?')
mahalla=input('Mahallangiz nima?')
tuman=input('Tumaningiz nima?')
viloyat=input('Viloyatingiz nima?')
print(kocha+' ko`chasi,',mahalla+' mahallasi,',tuman+' tumani,',viloyat+' viloyati.')
 
name=input('What is your name?')
print('Good morning'+name)
health=input('How are you?')
print("Wwow that is amazing to feel " +health)