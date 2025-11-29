#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 00:28:14 2025

@author: samandaroripov
"""
# FUNKSIYA VA RO`YXAT
# Funksiyaga ro`yxat uzatish

def katta_harf(matnlar):
    kattaharf=[]
    while matnlar:
        matn=matnlar.pop()
        kattaharf.append(matn.capitalize())
    return kattaharf

matnlar=['alisher navoiy','sam oripov','temur malik']
print(katta_harf(matnlar[:]))

def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()   

ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)

def katta_harf(matnlar):
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()
    return matnlar

ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)

def bahola(ismlar):
    baholar = {}
    for i in ismlar: 
         
        baho= input(f"Talaba {i.title()}ning bahosini kiriting: ")
        baholar[i]=baho
    return baholar
talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)





















