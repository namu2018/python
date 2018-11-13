# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 09:14:34 2018

@author: ktm
"""


class FourCal:
    def setdata(self,first,second):
        self.first=first
        self.second=second
   
    def print_var(self):
        print(self.first, self.second)
    
    def sum(self):
        return self.first+ self.second
    
    def minus(self):
        return self.first - self.second
    
    def gob(self):
        return self.first*self.second
    
    def nanu(self):
        return self.first / self.second
    
a=FourCal()
a.setdata(4,2)
a.print_var()
a.sum()
a.nanu()

###클래스의 생성자
##생성자(constructor)객체가 생성될때 자동으로 호출되는 매서드를 말한다
class FourCal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
   
    def print_var(self):
        print(self.first, self.second)
    
    def sum(self):
        result=self.first+ self.second
        return result
    
    def minus(self):
        return self.first - self.second
    
    def gob(self):
        return self.first*self.second
    
    def nanu(self):
        return self.first / self.second

b=FourCal(4,6)
b.sum()

