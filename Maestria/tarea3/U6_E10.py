#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 16:12:10 2021

@author: mating
"""
import numpy as np 
import matplotlib.pyplot as plt 

from Interpolation import Interpolation

T=[0,0.0526,0.1053,0.1579,0.2105,0.2632,0.3158,0.3684,0.4211,0.4737,
0.5263,0.5789,0.6316,0.6842,0.7368,0.7895,0.8421,0.8947,0.9474,1]

S_t=[0,0.8970,-0.1333,-0.7069,0.2131,0.5410,-0.2531,-0.4007,0.2646,
0.2853,-0.2568,-0.1930,0.2367,0.1211,-0.2098,-0.0670,0.1799,0.0275,
-0.1498,0]

m=500

T=np.array(T); S_t=np.array(S_t);
samples=np.linspace(0.0,1.0,m)

datas={'data':(T,S_t),'n':len(T)-1}
Pol=Interpolation(datas)
coef=Pol.Vandermode()


pol_fit=np.zeros_like(samples)
for i in range(len(T)):
    pol_fit+=coef[i]*samples**i
    
plt.plot(T,S_t,marker='*',color='red',linestyle=' ',markersize=10,label='Muestras')
plt.plot(samples,pol_fit,color='black',label='Vandermode')
plt.grid()
plt.title(" Interpolación con Vandermode",fontsize=14)
plt.xlabel(" x",fontsize=14)
plt.ylabel(" y",fontsize=14)
plt.legend()
plt.show()

Scoef=Pol.CubicSplines()
mm=int(m/len(T));

for i in range(len(T)-1):
    samples=np.linspace(T[i],T[i+1],mm)
    pol_fit=Scoef['a_j'][i]+Scoef['b_j'][i]*(samples-T[i])\
    +Scoef['c_j'][i]*(samples-T[i])**2+Scoef['d_j'][i]*(samples-T[i])**3
    plt.plot(samples,pol_fit,color='black')
    
plt.plot(T,S_t,marker='*',color='red',linestyle=' ',markersize=10,label='Muestras')
plt.grid()
plt.title(" Interpolación con splines",fontsize=14)
plt.xlabel(" x",fontsize=14)
plt.ylabel(" y",fontsize=14)
plt.legend()
plt.show()
    