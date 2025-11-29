#5-dars String Matn
matn='men yangi 🚗 sotib oldim '
print(matn)
ism='Samandar'
print('Mening ismim'+' '+ ism) # ikki so`z orasiga bo`sh joy
ism='Samandar'
familiya='Oripov'
print(ism+familiya)
print(ism+" "+familiya)

ism='Samandar'
familiya='Oripov'
ism_familiya=f"{ism}  {familiya}"# f-string matnlarni bir biriga qoshishda
print(ism_familiya)
ism='James'
familiya='Bond'
print(f'Salom,Mening ismim {familiya}.{ism} {familiya}!')
print('SamnadarOripov')
print('Samandar\tOripov') #\t so`z orasiga bosh joy
print('Samandar\nOripov') # \n yangi qator hosil qiladi

#upper() and lower() metodlari
print(ism_familiya.upper()) #upper string metodi har bir harf katta
print(ism_familiya.lower()) #lower string metodi har bir harf kichik

#title va capitalize methods
print(ism_familiya.title()) # matndagi har bir so`z birinchi harfi katta
ism_familiya='oripov samandar'
print(ism_familiya.capitalize()) #brinchi so`z bosh harfi katta
print('Men olma daraxtini ekdim'.upper(),'VA MAZZA QILIB OLMA YEDIM.'.lower())
print('kecha uyga bordim,'.title(),'noutbukda Vazifamni Tayyorladim'.capitalize())

#strip(), rstrip(),lstrip
meva="   olmani   "
print("Men"+" "+meva.lstrip() + "yaxshi ko`raman.") # lstrip() matn boshidagi bo`shliq
print("Men" + meva.rstrip()+" "+"yaxshi ko`raman.") # rstrip() matn oxiridagi bo`shliq
print("Men"+" "+meva.strip()+" "+"yaxshi ko`raman") # strip() matn boshi va oxiridagi bo'shliq

#input
ism=input('Ismingiz nima?')
print('Assalamu alaykum,'+ism.title())
ism=input('Ismimgiz nima?\n')
print('Assalamu alaykum '+ism.title())
ahvol='yaxshi'
ahvol=input('Qandaysiz?\n')
print('Men ham '+ahvol)
















