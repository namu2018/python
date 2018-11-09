# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:01:05 2018

@author: ktm
"""
"""
while ( 조건문  ):
    실행문1
    실행문2
    실행문3

조건문이 false가 될때까지 실행

c=0 
while(c<5):
    print(c)
    c=c+1
print("end")

num=int(input())
while(num !=0):
    print(1)
    num=int(input())
print("end")

"""
i=0
sum=0
while i<100:
    i=i+1
    sum +=i
print(sum)

i=0
sum=0
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
while i < len(A):
    if A[i] >= 50:
        sum=sum+A[i]
    i=i+1
print(sum)
    
i=0   
for i in range(0,100):
    i=i+1
    print(i,end='')
    
sum=0
i=0
for i in range(0,1000):
    i=i+1
    if i%5==0:
        sum +=i
        print(i)
print(sum)


blood = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
i=0; Asum=0; Bsum=0; Osum=0; ABsum=0
for b in blood:
    if b=='A':
        Asum = Asum +1
    elif b=='B':
        Bsum=Bsum+1
    elif b=='O':
        Osum=Osum+1
    elif b=='AB':
        ABsum=ABsum+1
print(Asum, Bsum, Osum, ABsum)
        
sum=0;
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
for i in A:
    if i > 30 :
        sum=sum+i
    i=i+1
print(sum)
    

data = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
result = {}
for blood_type in data:
    if blood_type in result:  # 키 값이 존재하는 경우에는 기존 값에 더함
        result[blood_type] += 1
    else:  # 키 값이 없는 경우에는 새로운 키 생성
        result[blood_type] = 1

print(result)  # {'A': 3, 'B': 3, 'O': 3, 'AB': 3} 출력
    

