# -*- coding: utf-8 -*-
#%%

##전역변수
result1=0
result2=0
result3=0
result4=0
result5=0

#%%
##첫번째 덧셈 계산기
def sum1(num):
    global result1
    result1 += num
    return result1
#%%
##두번째 덧셈 계산기
def sum2(num2):
    global result2
    result2 += num2
    return result2

def sum3(num3):
    global result3
    result3 -= num3
    return result3

def sum4(num4):
    global result4
    result4 *= num4
    return result4

def sum5(num5):
    global result5
    result5 //= num5
    return result5

#%%
sum1(9)
sum2(8,3)
#%%
