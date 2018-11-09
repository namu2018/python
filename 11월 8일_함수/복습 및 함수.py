# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:13:37 2018

@author: ktm
"""
##문자열 삽입 join
##문자열 나누기 split
abc="today is good"
abc.split()
a=":"
a.join(abc)

'''
함수형식1
def fnc1():
    print('a') ##화면에 출력
    
함수형식1
def func2():
    return '1' ##사용한 주최한테 값을 반환한다
    
함수형식3
def func3(a,b):
    return a+b   ###값을 전달 받아서 반환한다

함수형식4
def func4(a,b,c=0,d=0,e=0,f=0,) ##매개변수의 초기값 설정: 설정이 있으면 생략 가능
    return 
'''

def minus(a,b):
    return a-b
c=minus(4,5)
c


def even_sum(*arg):
    result = 1 
    i=0
    for i in arg: 
         if i%2==0:
               result = result * i 
    return result 
           
even_sum(3,4,5,6,7,8,)






#####결과값을 두개 전달하는 함수 만들기
def func(*arg):
    return max(arg), min(arg)

func(2,3,4,5,6,7,8,9,10)


minus=lambda a,b:a-b

##구구단
def gugudan(n):
    i=1
    for i in range(1,10):
        print("%d * %d = %d" % (i,n,i*n))
    

gugudan(3)

########################################3
list[ lambda a,b:a+b , lambda a,b:a-b, lambda a,b:a*b, lambda a,b:a//b ]
###########################################
def gugu(n1, n2):
    i=1;j=1
    for i in range(1,10):
        print("%d * %d = %d" % (i,n1,i*n1))
        
    for j in range(1,10):
        print("%d * %d = %d" % (j,n2,j*n2))
    
    
gugu(2,3)
