#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  8 11:50:35 2025

@author: samandaroripov
"""

# class name: def __init__(self)
# pass operatori

class User:
    def __init__(self,ism,familiya,age,country):
        self.ism=ism
        self.familiya=familiya
        self.age=age
        self.country=country
    
    def get_info(self):
        return f"Foydalanuvchi: Ismi {self.ism},familiyasi {self.familiya},yoshi {self.age}, vatani {self.country}"
                     


user1=User('SAM','ORIPOV',21,"UZBEKISTAN")
print(user1.get_info())
















