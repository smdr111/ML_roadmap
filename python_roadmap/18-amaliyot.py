# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 08:18:05 2023

@author: User
"""
# 1-masala
print('Buyurtma nomini kiriting.')
buyurtmalar=[]
n=1
while True:
    savol=input('Nima buyurtma qilasiz:')
    print(f'{n}-buyurtma qabul qilindi.')
    n+=1
    buyurtmalar.append(savol)
    javob=input('Yana buyurtma qo`shasizmi?(ha/yo`q)')
    if javob=='ha':
        continue
    else:break
print('Buyurtmalaringiz ro`yxati:')
for buyurtma in buyurtmalar:
    print(buyurtma.title())
    
# 2-masala

print('Mahsulotingiz nomini va narhini kiriting.')
mahsulotlar={}
m=1
while True:
    savol=input(f'{m}-mahsulot nomini kiriting:')
    narh=input(f"{savol.title()}ning narhini kiriting:")
    print('Mahsulot narhi va nomi qabul qilindi.')
    m+=1
    mahsulotlar[savol]=narh
    javob=input('Yana mahsulot qo`shasizmi?(ha/yo`q)')
    if javob=="ha":
        continue
    else:
        break
print('Mahsulotlaringiz ro`yxati:')
for k,v in mahsulotlar.items():
    print(f'{k.title()} {v}')

# 3-masala

buyurtmalar=['olma', 'banan', 'olcha', 'nok']
mahsulotlar={'olma': '5000 so`m', 'banan': '6000 so`m', 'ece': 'ccccwec', 'cewc': 'xe'}

for buyum in buyurtmalar:
    if buyum in mahsulotlar:
        print(f"{buyum.title()} {mahsulotlar[buyum]}.")
    if not buyum in mahsulotlar:print(f'Bizda {buyum} yo`q.')
# 2-usuli

buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")
































