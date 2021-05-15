# -*- coding: utf-8 -*-
"""
@author: MADZEROPIE
"""

from random import random, seed
seed(10)
import pandas as pd
import matplotlib.pyplot as plt
import math

N = 1000009 #число экспериментов

#lam=float(input("Введите параметр лямбда: "))
lam=0
while lam<1:
    lam=float(input("Введите параметр лямбда: "))

b=1-1/lam
#print(b)
#print()


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

#print(arr)
print()
print()

def M() -> float:
    return 4/3*al*al-2*al*al+1/(lam*lam)

def x_() -> float:
    sum=0
    for el in arr:
        sum+=el
    return sum/N

def D() -> float:
    M__=M()
    return 1/12*8*al*al*al+2/(lam*lam*lam) - M__*M__

def S2() -> float:
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

def Me() -> float:
    if N%2==0:
        return (arr[N//2-1]+arr[N//2])/2
    else:
        return arr[N//2]
    
def R() -> float:
    return arr[N-1]-arr[0]

        
print("Me", Me())
print()
print("R", R())      
print()



#data = pd.DataFrame(columns=['M','Выб. среднее', 'D', 'Выб. дисперсия', 'Размах', 'Медиана'],  data=[[M(), x_(), D(), S2(), R(), Me()]])
#data['|M - x_|'] = abs(M() - x_())
#data['|D - S2|'] = abs(D() - S2())
#print(data)

def f(x:float) -> float:
    if(x<0):
        return x/(2*al)+1
    else:
        return math.exp(-lam*x)

def f1(x:float) -> float:
    if(x>b):
        return ((-1/lam) * math.log(lam*(1-x)))
    else:
        return 2*math.sqrt(al*x)-2*al



#z = [-1,  -0.7,  -0.5, -0.3, -0.15, -0.05, 0.0, 0.01,  0.1, 0.15, 0.16, 0.35,0.3501, 0.45, 0.55, 0.78,0.85, 1.0, 2.0, 3.0, 4, arr[N-1]]
#k = len(z)

k = int(N**(1/3))
z=[0]*(k+1)
for i in range(k):
    z[i]=f1(i/k)
z[-1]=arr[-1]

k = len(z)

z2 = [0]*(k-1)
li = [0]*(k-1)

for i in range(len(z)-1):
    z2[i]=(z[i]+z[i+1])/2
    li[i]=z[i+1]-z[i]


#print(z)

bins=[0]*(k-1)

for a in arr:
    #print(a)
    for j in range (0, len(z)-1):
        if (a>z[j]) & (a<=z[j+1]):
            bins[j]+=1
            #print(j)
            break

        
#print(bins)
#print()

bins2=[0]*(k-1)
for i in range(len(bins)):
    bins2[i]=bins[i]/(N*li[i])

fnj=[0]*(k-1)
for i in range (k-1):
    fnj[i]=f(z2[i])

#print(z2)
#print(bins2)
#print(fnj)

max_diff=0
for i in range(len(bins2)):
    max_diff=max(abs(bins2[i]-fnj[i]), max_diff)
print("max_diff = ",max_diff)

plt.figure(figsize=(10, 5))
plt.step(z2, fnj, label='Theory')
plt.step(z2, bins2, label='Practice')
plt.title('Distribution Function')
plt.legend()
plt.grid()
plt.show()

def qj(lb: float, rb: float) -> float:
    if lb<-2*b:
        lb=-2*b
    if lb<0 & rb>0:
        return qj(lb,0)+qj(0,rb)
    if lb < 0:
        return (rb*rb-lb*lb)/(4*al)+rb-lb
    else:
        return (-1/lam)*(math.exp(-lam*rb)-math.exp(-lam*lb))

def R0():
    ans = 0
    for i in range(k-1):
        nqj = bins[i] * qj(z[i], z[i+1])
        ans += ((N-nqj)**2)/nqj
    

alf=0.05

