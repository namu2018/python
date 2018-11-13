# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 10:44:00 2018

@author: ktm
"""

class common():
    def __init__(self, name='무명'):
       self.name=name
    def walk(self):
        print("걷는다")
    def eat(self):
        print("먹는다")
    def sleep(self):
        print("잠잔다")
    def greet(self):
        print("{}가 인사한다" .format(self.name))
        
class Human(common):
    def wave(self):
        print("손을 흔든다")
    def sleep(self):
        print("누워잔다.")
    def greet(self):
        print(self.name)
        self.wave()
        super().greet()
        
class Dog(common):
    def wag(self):
        print("꼬리를 흔든다")
    def sleep(self):
        print("엎드려잔다.")

class bird(common):
    def wag(self):
        print("꼬리를 흔든다")

p1=Human("철수")
p1.greet()
