# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 23:49:16 2023

@author: User
"""

# 1-masala
otam={'Ismi':'Iskandar','Familiya':'Normatov','t_yil':'1984','t_joy':'Uzbekistan'}
print(f"Menig otam {otam['Ismi'].title()} {otam['Familiya'].title()}.\
U {otam['t_yil']}-yilda {otam['t_joy']}da tug`ilgan")

# 2-masala
taom={
      'Iskandar':'Manti',
      'Nazokat':'Osh',
      'Samandar':'Bosma',
      'Munisa':'Kebab',
      'Orifjon':'G`osht'
      }
print(f"{taom['Iskandar']}\n{taom['Munisa']}\n{taom['Samandar']}")

# 3-masala
atamalar={'int':'butun son','float':'O`nlik son','title':'Bosh harf',\
       'str':'matn','upper':'hammasi katta harf','lower':'hammasi kichik harf',\
        'remove':'qiymat boyicha o`chiradi','del':'indeks bo`yicha o`chiradi',\
            'list':'ro`yxat','type':'o`zgaruvchi turini tekshirish'}

# 4-masala
atama=input('Biror so`z kiritng:\n')
if atama.lower9() in atamalar:print(atamalar[atama])
else:print('Bunday so`z mavjud emas.')

# 2-usuli
kalit = input("Kalit so'z kiriting:").lower()
tarjima = atamalar.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
    
# 5-masala
soz=input('Biror so`z kiriting:\n').lower()
kalit=atamalar.get(soz,'Bunday s`oz mavjud emas')
print(kalit)













