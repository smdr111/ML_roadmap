# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 06:57:00 2023

@author: User
"""
# 1-masala
kitob=('Yaxshi ko`rgan kitoblaringiz nomini kiriting')
kitob+='(dasturni tugatmoqchi bo`lsangiz stop so`zini kiriting:)'

while True:
    kitob_nomi=input(kitob)
    if kitob_nomi=='stop':
        break
print('Rahmat')

# 2-masala
savol='Yoshingiz nechada:'

while True:
    yosh=input(savol)
    if yosh=='stop' or yosh=='quit':
        break
    yosh=int(yosh)
    if yosh<=7:print('Sizga kirish 2000 s`om')
    elif 7<yosh<18:print('Sizga kirish 3000 so`m')
    elif 18<=yosh<=65:print('Sizga kirish 10000 so`m')
    elif 65<yosh:print('Sizga kirish bepul')
    
print('Rahmat') 

# 2-usuli
savol = "Yoshingizni kiriting: "

while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(qiymat)
    
    if yosh<7:
        narh = 2000
    elif 7<=yosh<18:
        narh = 3000
    elif 18<=yosh<65:
        narh = 10000
    else: narh = 0
    
    if narh==0:
        print("Sizga chipta bepul")
    else:
        print(f"Chipta {narh} so'm")
        
# 3-masala

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    qiymat=int(qiymat)
    if qiymat>0:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning kvadrat ildizi {ildiz} ga teng")
        continue
    
    else:
       print('Musbat son kiriting')
print('Rahmat!')

# 2-usuli

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
    























