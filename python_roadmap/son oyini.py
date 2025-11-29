#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 12:46:08 2025

@author: samandaroripov
"""
import random as r
def son_top(x=10):       
        print('Keling o`ylagan sonni topish o`ynaymiz!')
        son1=r.randint(1,x)
        son2=int(input(f'1 dan {x} gacha son o`yladim topa olasizmi:\n>> ')) 
        n=1
        while True:
              if son1>son2:son2=int(input('Xato,men o`ylagan son bundan kattaroq,Yana harakat qiling:\n>>' ))
              elif son1<son2: son2=int(input('Xato,men o`ylagan son bundan kichikroq,Yana harakat qiling:\n>>')) 
              else: break
              n+=1  
        print(f'Topdingiz! {son2} ni o`ylagan edim.{n} ta taxmin bilan topdingiz. Tabriklayman!')  
        return n
    
 
def son_toppc(x=10):
        input(f'1 dan {x} gacha son o`ylang men taxmin qilaman.'
              'Son o`ylagan bo`lsangiz istalgan tugmani bosing: ')
        l=1
        min=1
        max=x               
        while True:
            if min!=max:
                son3=r.randint(min,max)
            else:
                son3=1
            javob=input(f'Siz {son3} sonni o`yladingiz:\n'
                        'tog`ri(T),men o`ylagan son bundan kattaroq(+)\n'
                        'men o`ylagan son bundan kichiqroq(-)?'.lower())
            if javob=='+':min=son3+1
            elif javob=='-': max=son3-1
            else:break
            l+=1
        print(f'Soningizni {l} ta taxmin bilan topdim.')
        return l
savol=True
while savol:
        n=son_top()
        l=son_toppc()
        if n>l:print(f'Siz yutqazdingiz,sizda {n} ta taxminlar soni menda esa {l} ta.')  
        elif n<l:print(f'Siz yutdingiz,sizda {n} ta taxminlar soni menda esa {l} ta.') 
        else:print(f'Durrang! Ikkimiz ham {n} ta taxmin bilan topdik')
        savol=int(input('Yana o`ynaymizmi:ha(1) / yo`q(0):'))
        












         





























