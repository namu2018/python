# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 09:48:30 2018

@author: ktm
"""
##########객체를 만들떄 버튼의 갯수를 처음부터 지정
class Human():
    def walk(self):
        print("걷는다")
        
    def eat(self):
        print("먹는다")
    
    def wave(self):
        print("손을 흔든다")

class Dog():
    def walk(self):
        print("걷는다")
    
    def eat(self):
        print("먹는다")
    
    def wag(self):
        print("꼬리를 흔든다")


person1=Human()
person1.walk()
person1.eat()
person1.wave()

person2=Human()
person2.eat()
person2.walk()
person2.wave()

dog1=Dog()     
dog1.walk()
dog1.eat()
dog1.wag()


class common():
    def walk(self):
        print("걷는다")
        
    def eat(self):
        print("먹는다")
        
###common이라는 클래스를 상속받는다
        
class Human(common):
    def wave(self):
        print("손을 흔든다")

class Dog(common):
    def wag(self):
        print("꼬리를 흔든다")