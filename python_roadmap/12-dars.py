# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 23:43:56 2023

@author: User
"""
# Xatolar bilan ishlash
# sytax error-sinteks xato
# eol(end of line) va eof(end of function) errors
# Indentation error-Joy tashlashda xatolik
# RUN TIME ERRORS-Dasturni bajarishda xartoliklar:
# type error-biror funsiya yoki metodda xatolik
# Name error-O'zgaruvchi, funktsiya, obyekt nomini noto'g'ri yozish natijasida kelib chiquvchi xatolik.
# Value error-Funktsiyaga noto'g'ri qiymatni yuborish natijasidagi xatolik
# Index error indeksdagi xatolik 
# Mantiqiy xatolik Mantiqiy xatolar - dasturchi tomonidan yo'l qo'yilgan va kutilgan natijani 
#berishda to'sqinlik qiluvchi xatolar. Bunday xatolar eng ko'p uchraydigan va aniqlash 
#eng qiyin bo'lgan xatolar hisoblanadi. Aksar holatlarda Python mantiqiy xatolarni aniqlamaydi 
#va dastur bajarilaveradi (lekin kutilgan natija chiqmaydi).

# AMALIYOT
# 1-masala
son=float(input("Juft son kiriting: "))
if son%2:# Agar sonni ikkiga bo`lganda qoldiq qolsa
    print("Bu son juft emas.")
else:
    print("Rahmat!")
    
# 2-masala
yosh=int(input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    narh=0
elif yosh<18:
    narh=10000
else:
    narh=20000
print(f"Chipta {narh} so'm")

# 3-masala
x=float(input("Birinchi sonni kiriting: "))
y=float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")

# 4-masala
mahsulotlar=['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

savat=[]
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else: 
    print("Savatingiz bo'sh")       
    
# 5-masala
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
      print("Do'konimizda quyidagi mahsulotlar yo'q:")
      for mahsulot in mavjud_emas:
               print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
  
# 6-masala
users = ['alisher1983','aziza','yasina' 'umar']

login = input("Yangi login tanlang:" )

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        