# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 04:29:25 2023

@author: User
"""

# IF,ELIF,ELSE
yosh = int(input('Yoshingiz nechida? '))
if yosh<=4:narh=4000
elif yosh<=16:narh=8000
elif yosh<=20:narh=10000
else:narh=12000
print(f'Sizga kirish {narh} so`m')

# AND va OR operatorlari
# or operatori shartlardan biri bajarilsa TRUE bo`ladi
pasword=input('Maxfiy so`zni kiriting:')
if pasword.lower()=='sam' or pasword.lower()=='fox':print(f'Welcome {pasword.title()}!')
else:print('Can not be found!')

name=input('What is your name?\n ')
surname=input('What is your surname?\n ')
if name.lower()=='sam' or surname.lower()=='oripov':print(f'Assalamu alaykum,{surname.title()}')
else:print('Does not match')

# and operatorida esa hamma shart bajarilganda TRUE bo`ladi 
ism=input('Ismingizni kiriting:\n')
yosh=int(input('Yoshingizni kiriting:\n'))
if ism.lower()=='sam' and yosh>=18:
    print(f'Welcome {ism.title()}')
elif ism.lower()=='sam' and yosh<18:
    print(f'Sorry {ism.title()},age limit is not enough')
else:print(f'Sorry {ism} does not match')

# and va or birgalikda
mahsulot=input('Nima sotib olmoqchisiz?\n')
son=int(input(f'Nechta {mahsulot} sotib olmoqchisiz?\n'))
if (mahsulot.lower()=='olma'or mahsulot.lower()=='banan'or mahsulot.lower()=='olcha') and son<=5:
    print(f'{son} ta {mahsulot.lower()} sotib oldingiz!')
elif (mahsulot.lower()=='olma'or mahsulot.lower()=='banan'or mahsulot.lower()=='o`rik') and son>5:
    print(f'Uzr,bizda {son} ta {mahsulot.lower()} yo`q')
else:(f'Uzr,bizda {mahsulot.lower()} mavjud emas')

mevalar=input('Qanday meva sotib olmoqchisiz?\n')
son1=int(input(f'Nechta {mevalar} sotib olmoqchisi\n'))
if mevalar.lower()=='banan':narh=(son1*5000)
elif mevalar.lower()=='olma':narh=(son1*8000)
elif mevalar.lower()=='olcha':narh=(son1*7500)
print(f'{son1} ta {mevalar} sotib oldingiz.\nJami {narh} so`m.\nXaridingiz uchun rahmat!')

# BOOLEN mantiqiy qiymatlar TRUE/FALSE va 1/0
narh=2200
iphone=True
ipad=False
watch=True
if iphone:narh=1700
if iphone and watch:narh=narh+1700+800
print(f'Jami {narh} so`m')

narh=2000
tel=1
soat=0
planshet=0
naush=1
if tel:
     print('Mijoz telefon sotib oldi')
     narh=narh+300
if soat:
   print('Mijoz soat ham sotib oldi')
   narh=narh+100
if planshet:
       print('Mijoz planshet sotib oldi')
       narh=narh+500
if naush:
       print('Mijoz quloqchin sotib oldi')
       narh=narh+50
print(f'Jami {narh} so`m')

# Ro`yxat tarkibini tekshirish
# IN operatori

gullar=['lola','paxta','atirgul','boychechak','kaktus']
print('sam'in gullar)
gul=input('Qanday gul sotib olmoqchisiz?\n')
if gul in gullar:print(f'Siz {gul} sotib olmoqchisiz, narhi 5000 so`m.')
else:print('Kechirasiz bizda bunday gul yo`q.')

# NOT IN operatorida esa teskarisi
# NOT operatorini boshqalari bn ham ishtsh mkn msl ucn if not a==5 <-> if a!=5

# ikki ro`yxatni solishtirish

gullar_royxati=['lola','paxta','atirgul','boychechak','kaktus']
klent=['lola','atirgul','kaktus','olma']
for gul in klent:
    if gul in gullar_royxati:print(f'Bizda {gul} bor')
    else: print(f'Kechirasiz bizda bunday {gul} yo`q')

# ro`yxat bo`sh emasligini tekshirish
gullar_royxati=['lola','paxta','atirgul','boychechak','kaktus']
klent=[]
if klent:
   for gul in klent:
    if gul in gullar_royxati:print(f'Bizda {gul} bor')
    else: print(f'Kechirasiz bizda bunday {gul} yo`q')
else:print('Siz hech narsa buyurtma bermadingiz.')

# Demak ro`yxat boshligini IF ROYXAT NOMI bn tekshirish mumkin









