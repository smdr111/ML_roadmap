#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 14:15:01 2025

@author: samandaroripov
"""
# Moslashuvchan funksiya 
# *args 1 qiymat va **kwargs lug`at ko`rinishida

def kopaytir(*sonlar):
    a=1
    for son in sonlar:
        a=a*son

    return a

b=kopaytir(1,2,3,4)
print(b)

def talaba_info(ismi,familiyasi,**malumotlar):
    malumotlar['Ismi']=ismi
    malumotlar['Familiyasi']=familiyasi
    return malumotlar 
talaba=talaba_info('Samandar','Oripov',yoshi=21,millati='Uzbek',t_joy='Bagdod')
print(talaba)











