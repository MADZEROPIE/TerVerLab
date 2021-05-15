# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 21:18:12 2021

@author: MADZEROPIE
"""

from random import random, seed
import pandas as pd
import matplotlib.pyplot as plt
import math
from datetime import datetime

alf = 0.05
co=0
b=0.5
print("alfa = ", alf)

def f1(x:float) -> float:
    if(x>b):
        return ((-1/lam) * math.log(lam*(1-x)))
    else:
        return 2*math.sqrt(al*x)-2*al
    


for ii in range(20):
    seed(datetime.now())
    
    N = 1000 #число экспериментов
    
    
    lam = 2
    al=b=1-1/lam
    
    arr = [0]*N
    al=1-1/lam
    
    
    for i in range(N):
        x=random()
        if(x>=b):
            arr[i]=((-1/lam) * math.log(lam*(1-x)))
            if(arr[i]<0):
                print("ERROR")
        else:
            arr[i]=2*math.sqrt(al*x)-2*al
            if(arr[i]>0):
                print("ERROR")
          
    arr.sort()
    
    def qj(lb: float, rb: float) -> float:
        if rb<=-2*b:
            return 0.0
        if lb<-2*b:
            lb=-2*b
        if lb<0 and rb>0:
            return qj(lb,0)+qj(0,rb)
        if lb < 0:
            return (rb*rb-lb*lb)/(4*al)+rb-lb
        else:
            return (-1/lam)*(math.exp(-lam*rb)-math.exp(-lam*lb))
    
    
    
    z = [-math.inf,  -0.75,  -0.6, -0.375, -0.2,  0.0, 0.125, 0.25, 0.375, 0.6, 0.9, arr[N-1]-3, math.inf] #12
    k1 = 13
    z[0]=f1(0)
    for i in range(1,k1-1):
        z[i]=f1(i/(k1-1))
    z[-1]=math.inf
    print(z)
    print(arr[-1])
    
    bins=[0]*(k1-1)
    
    for a in arr:
        #print(a)
        for j in range (0, len(z)-1):
            if (a>z[j]) & (a<=z[j+1]):
                bins[j]+=1
                #print(j)
                break
    
    print(bins)
    
    def R0() -> float:
        ans = 0
        for i in range(k1 - 1):
            nqj = N * qj(z[i], z[i+1])
            ans += ((bins[i]-nqj)**2)/nqj
        return ans
        
    
    
    print("k-1 = ", len(z)-2)
    chi_square_val = 19.675
    print("R = ", R0())
    print("chi_square_val =", chi_square_val)
    if R0()<chi_square_val:
        co+=1
    
print(co,'/',20)
