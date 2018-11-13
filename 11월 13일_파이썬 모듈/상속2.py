# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 10:16:25 2018

@author: ktm
"""

class Car():
    def run(self):
        print("차가 달립니다")
    def stop(self):
        print("차가 멈춥니다")
    def move(self):
        print("차가 움직입니다")
        
class Truck(Car):
    def load(self):
        print("트럭이 짐을 싣다")
        
class Taxi(Car):
        
    def carry(self):
        print("고객을 실어 나르다")

class Taxi_M(Taxi):
    def good_M(self):
        print("친절하고 안전하다")
        
    def fee_M(self, fee):
        self.fee=fee
    
 
class Taxi_G(Taxi):
    def good_G(self):
        print("적당히 친절하고 적당히 싸다")
        
    def fee_G(self, fee):
        self.fee=fee
      
        
c1=Truck()
c1.run()
c1.load()
c1.stop()

c2=Taxi_G()
c2.good_G()
c2.fee_G(3)
c2.fee
