# -*- coding: utf-8 -*-


#  LIST

mevalar=['olma','orik','shaftoli','banan'] # matn ko`rinishida
sonlar=[1200,1654,78,5879] # son ko`rinishida
raqamlar=['Bir','ikki',3,4]# aralash ko`rinishda
ism=[] # bo`sh holatda ham bo`lishi mumkin
# listdagi o`zgaruvchini nomlashda -lar (ko`plik) da belgilash yaxshi

# List elementlar INDEX

mevalar=['olma','orik','shaftoli','banan']
print('Birinchi meva:',mevalar[0]) # Listdagi birinchi har doim 0 dan b-di
print('Ikkinchi meva:',mevalar[1])

# agar list matnlardan iborat bo`lsa, string metodlarni qo`llash mumkin
print('Uchinchi meva:',mevalar[2].upper())
print('To`rtinchi meva:', mevalar[3].capitalize())
print(mevalar[3].upper())
print('Samandar'.upper())

#elementlar ustida arifmetik amallar
narhlar=[1500,1980,3000,7980,2415]
print(narhlar[0]+narhlar[3])

#listning eng oxiridagi elementga -1 indeksi ishlatish mumkin 
print(mevalar[-1])
print(narhlar[-1])

# Listdagi elementni o`zgartirish
ismlar=['Ali','Vali','Ra`no', 'G`ani']
ismlar[0]='Sam'
ismlar[3]='Tom'
print(ismlar) # indeksi bo`yicha murojaat qilamiz va yangi qiymat yuklaymiz

# Listga yangi element qo`shish: append() va insert() metodlari
kunlar=['Du','Cho','Pa','JU']
kunlar.append('Sha')
kunlar.append('Ya')
print(kunlar) # append metodi listning OXIRIGA yangi element qo`shadi
cars=[]
cars.append('nexia')
cars.append('Lambo')
cars.append('Bugatti')
cars.append('Ferrari')
print(cars)
# insert metodi matnning ISTALGAN joyiga element qo`shadi
colors=['blue','pink','yellow']
colors.insert(0,'black')
colors.insert(4,'white')
print(colors)
print(colors[-1])

# Listdagi elementni o`chirish: del va remove
qushlar=['ukki','burgut','qarg`a','chumchuq']
del qushlar[3] # del INDEKS bo`yicha o`chiradi va matn boshidan yoziladi
print(qushlar)
gullar=['lola', 'atir','paxta']
gullar.remove('paxta')# remove qiymati bo`yicha olib tashlaydi
print(gullar)
gullar1=['lola','atir','paxta','lola']
gullar1.remove('lola')
print(gullar1)

# Listdagi elementni sug`urib olish pop(index)
bozorlik=['un','yog`','guruch','go`sht','piyoz']
mahsulot=bozorlik.pop(3)# pop() da index berilmasa oxirgi elementni tanlab oladi
print('Kecha bozorlikka '+mahsulot+' sotib olmadim.',bozorlik,' sotib oldim.')













