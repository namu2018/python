# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 11:45:40 2018

@author: ktm
"""

#%%
class Cal:
    def __init__(self):###고정시키는 값
        self.result = 0
    def add(self,num):
        self.result += num
        return self.result
#%%

cal1=Cal()
cal2=Cal()
cal3=Cal()

cal1.add(3)    
cal2.add(5)
cal3.add(11)    