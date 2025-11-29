# -*- coding: utf-8 -*-


# 1-masala

shaxs1 = {'ism': 'alisher', 'familiya': 'navoiy', 't_yil': 1441}
shaxs2 = {'ism': 'amir', 'familiya': 'temur', 't_yil': 1436}
shaxs3 = {'ism': 'zahiriddin', 'familiya': ' muhammad bobur', 't_yil': 1483}
shaxslar = [shaxs1, shaxs2, shaxs3]
for shaxs in shaxslar:
    print(f"{shaxs['ism'].title()} {shaxs['familiya'].title()},"
          f"{shaxs['t_yil']}-yilda tavvalud topgan.")

# 2-masala
shaxs1 = {'ism': 'alisher', 'familiya': 'navoiy', 't_yil': 1441,
          'asarlar':['hayrat-ul abror', 'sabbayi sayyor']}
shaxs2 = {'ism': 'amir', 'familiya': 'temur', 't_yil': 1436,
          'asarlar':['jang', 'temur tuzuklari']}
shaxs3 = {'ism': 'zahiriddin', 'familiya': ' muhammad bobur', 't_yil': 1483,
          'asarlar':['g`azallar to`lami', 'she`rlar toplami']}
shaxslar = [shaxs1, shaxs2, shaxs3]
for shaxs in shaxslar:
    print(f"\n{shaxs['ism'].title()} {shaxs['familiya'].title()},"
          f"{shaxs['t_yil']}-yilda tavvalud topgan."
          f"\nQuyidagi asarlari bor:{shaxs['asarlar']}")

# 3-masala

kino={
      'ali':['merlin','tarzan','yalmog`iz'],
      'vali':['suits','harry potter','witcher'],
      'gani':['gold','creed','batman']
      }
for ism,film in kino.items():
    print(f"\n{ism.title()}ning yoqtirgan kinolari:{film}")
    
# 4-masala
davlatlar={'Uzbekistan':{'mustaqil':1991,'ramzlari':['bayroq','gerb','madhiya'],'maydoni':144.48},
           'Russia':{'mustaqil':1966,'ramzlari':['baliq','ayiq'],'maydoni':1478788},
           'USA':{'mustaqil':1980,'ramzlari':['burgut','sher'],'maydoni':94494}
                  }
for davlat,info in davlatlar.items():
    print(f"\n{davlat.title()} {info['mustaqil']}-yilda mustqail bo`lgan."
          f"\nRamzlari {info['ramzlari']},maydoni esa {info['maydoni']} km kvadratni tashkil etadi.")

# 2-usuli

for davlat,info in davlatlar.items():
    print(f"\n{davlat.title()} {info['mustaqil']}-yilda mustqail bo`lgan."
          f"\nMaydoni esa {info['maydoni']} km kvadratni tashkil etadi.")
    print('Ramzlari esa quyidagilar:')
    for ramz in info['ramzlari']:
        print(ramz.title(), end=' ')

# 5-masala 
name=input('Qaysi davlat haqida ma`lumot bilishni xohlaysiz:\n>>>').lower()
if name in davlatlar:
        info=davlatlar[name]
        print(f"{name.title()} {info['mustaqil']}-yilda mustaqil bo`lgan."
              f"\nMaydoni esa {info['maydoni']} km kvadratni tashkil etadi.")
        print('Ramzlari esa quyidagilar:')
        for ramz in info['ramzlari']:
            print(ramz.title(),end=' ')
        
    
        






















