# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 08:22:19 2023

@author: User
"""

#9-Dars
# FOR va uning ishlatilishi

ismlar=['Davron','Ali','Vali','G`ani','Obid']
for ism in ismlar:
    print(ism)
cars=['Bmw','Lambo','Ferrari','Rolls','Bugatti']
for car in cars:
    print(f'Men kelajakda {car} sotib olaman.')
print('Chunki bular eng zo`ri')

# FOR yordamida sonli ro`yxat bilan ishlash

sonlar=list(range(5,21))
for son in sonlar:
    print(f'{son} ning kvadrati {son**2} ga teng')
    
# For yordamida ro`yxat ham yaratishmiz mumkin

numbers=list(range(16))
numbers_ikkilangani=[]
for number in numbers:
    numbers_ikkilangani.append(number*2)
print(numbers)
print(numbers_ikkilangani)

 # For va input
 
gullar=[]
print('Beshta gul nomini ayting') 
for gul in range(5):
    gullar.append(input(f'{gul+1} chi gul nomini ayting:'))
print(gullar)

runners=['SAM','TOM','TONY','KATE','MESSI']
for runner in runners,for k in range(1,6):
    print(f'Marraga {runner} {k} chi bo`lib yetib keldi')










