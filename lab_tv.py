# -*- coding: utf-8 -*-
"""
@author: MADZEROPIE
"""

from random import random, seed
seed(10)
import pandas as pd
import matplotlib.pyplot as plt
import math
import statistics

N = 11 #число экспериментов

lam=float(input("Введите параметр лямбда: "))

b=1-1/lam
#print(b)
#print()


arr = [0]*N
al=1-1/lam


for i in range(N):
    x=random()
    if(x>b):
        arr[i]=(-1/lam*math.log(lam*(1-x)))
    else:
        arr[i]=2*math.sqrt(al*x)-2*al
      
arr.sort()

print(arr)
print()
print()

def M():
    return 4/3*al*al-2*al*al+1/(lam*lam)

def x_():
    sum=0
    for el in arr:
        sum+=el
    return sum/N

def D():
    M__=M()
    return 1/12*8*al*al*al+2/(lam*lam*lam) - M__*M__

def S2():
    sum=0
    x__=x_()
    for el in arr:
        sum+=((el-x__)*(el-x__))
    return sum/N

print("X_", x_())
print("M", M())
print("|M - X_|", abs(x_()-M()))
print()


print("S2", S2())
print("D", D())
print("|D - S2|", abs(S2()-D()))
print()

def Me():
    if N%2==0:
        return (arr[N//2-1]+arr[N//2])/2
    else:
        return arr[N//2]
    
def R():
    return arr[N-1]-arr[0]

        
print("Me", Me())
print()
print("R", R())      
print()



#data = pd.DataFrame(columns=['M','Выб. среднее', 'D', 'Выб. дисперсия', 'Размах', 'Медиана'],  data=[[M(), x_(), D(), S2(), R(), Me()]])
#data['|M - x_|'] = abs(M() - x_())
#data['|D - S2|'] = abs(D() - S2())
#print(data)