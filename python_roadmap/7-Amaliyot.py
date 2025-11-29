# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 04:49:02 2023

@author: User
"""
# 1-masala
ismlar=['Anvar','Hasanboy','Obid']
print('Salom '+ismlar[0]+', bugun choyxonaga boramizmi?')
print(ismlar[1]+', choyxonga boramizmi?')
print('Qalaysan '+ismlar[2]+', bugun qayerga boramiz?')

# 2-masala
sonlar=[25,-78,6.8,-9832,57]
print(sonlar[1]*sonlar[4])
print(sonlar[2]+sonlar[3])

# 3-masala
t_shaxslar=['Amir Temur','Alisher Navoiy','Fitrat']
z_shaxslar=['Cristiano','Andrew','Elon']
shaxs1=t_shaxslar.pop(2)
shaxs2=z_shaxslar.pop(1)
print('Men tarixiy shaxslardan '+shaxs1+' bilan,','zamonaviy shaxslardan '+shaxs2+' bilan ko`rishmoqchi edim.')

# 4-masala
friends=[]
friends.append('Ilhom')
friends.append('Barno')
friends.insert(0,'Sam')
friends.append('Ali')
friends.insert(1,'Fox')
print(friends)
del friends[1]
friends.remove('Sam')
friends.insert(0,'Karl')
friends.insert(3, 'Vali')
friends.insert(5,'Vas')
print(friends)

# 5-masala
mexmonlar=[]
mex1=friends.pop(1)
mex2=friends.pop(3)
mex3=friends.pop(2)
mexmonlar.append(mex1)
mexmonlar.append(mex2)
mexmonlar.append(mex3)
print(mexmonlar)




