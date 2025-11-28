#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  5 00:22:53 2025

@author: samandaroripov
"""

import random as r
def get_word():           
         with open('words.txt','r') as file:
                word_list=[line.strip() for line in file]
         word=r.choice(word_list)
         return word
        

def display(word,letters=''):
    result=''
    for l in word:
        if l.lower() in letters.lower():
            result+=l
        else: result+='-'
    return result
            
def soz_play():
            word=get_word()
            print(f'Men {len(word)} ta harfli so`z o`yladim, topa olasizmi?')    
            print(display(word))
            harflar=[]
            n=0
            while True: 
                harf1=''
                harf=input('Harf kiriting: ')
                harflar.append(harf)
                for h in harflar:
                    harf1+=h
                result=display(word,harf1)
                if harf in word:
                    print(f'{harf} harfi to`g`ri\n {result}')
                else:
                    print(f'{harf} harfi noto`g`ri\n {result}')
                print(f'Shu vaqtgacha kiritgan harflaringiz: {harflar}')
                n+=1
                if result==word:
                    break
            print(f'Tabriklayman! {word} so`zini {n} ta urinishda topdingiz!')





