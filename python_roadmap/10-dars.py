# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 07:49:43 2023

@author: User
"""

# IF operatori

names=['Sam','Sarah','Nick','Tom','Tina']
for n in names:
    if n=='Sam': print(n.lower()) 
    else:print(n.upper())
    
# TRUE/False
car='lambo'
# == 'tengmi', !='teng emasmi'
name=input('The famous football player in the world?\nAnswer:')
if name.lower()!='ronaldo': print(f'{name.title()} is wrong answer') 
else:print('Your answer is correct')
    
# Sonlarni solishtirish
# a>b, a<b, a>=b, a<=b
javob=float(input('9 ning kvadrati nechiga teng?'))
if javob!=81:print('Xato javob') 
else:print('To`g`ri javob')

yosh=int(input('Yoshingizni kiriting:\n>>>'))
if yosh<18: print('Yosh chegarasi yetarli emas')
else:print('Assalamu alaykum,\nXush kelibsiz!')

# Bir qator IF/ELSE
son=int(input('Istalgan butun sonni kiriting:\n>>>'))
print(f'({son}) ning kubi ({son**3}) ga teng.') if son<0 else print(f'{son} ning kubi {son**3} ga teng')

















