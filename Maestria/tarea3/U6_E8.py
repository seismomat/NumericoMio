#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 01:28:39 2021

@author: mating
"""
import numpy as np 
import matplotlib.pyplot as plt 
from numpy import linalg as LA


class Interpolation:
    def __init__(self,datas):
        self.data = datas['data']
        self.n=datas['n']    
        
    def Vandermode(self):
        M=np.zeros((self.data[0].shape[0],self.n+1))
        
        for i in range(self.n+1):
            M[:,i]=self.data[0]**i
            
        print("Número de condición",LA.cond(M,2))
        return LA.solve(M,self.data[1])
    
    def Vandermode1925(self):
        M=np.zeros((self.data[0].shape[0],self.n+1))
        
        for i in range(self.n+1):
            M[:,i]=(self.data[0]-1925)**i
        print("Número de condición",LA.cond(M,2))

        return LA.solve(M,self.data[1])
    
    def Vandermode1960(self):
        M=np.zeros((self.data[0].shape[0],self.n+1))
        
        for i in range(self.n+1):
            M[:,i]=(self.data[0]-1960)**i
        print("Número de condición",LA.cond(M,2))
        return LA.solve(M,self.data[1])

T=[1930,1940,1950,1960,1970,1990,1995,2000]

S_t=[16552722,19653552,25791017,34923129,48225238,81249645,
91158290,97014867]

m=100

T=np.array(T); S_t=np.array(S_t);
samples=np.linspace(1930,2000,m)

datas={'data':(T,S_t),'n':len(T)-1}
Pol=Interpolation(datas)
coef=Pol.Vandermode1960()


pol_fit=np.zeros_like(samples)
for i in range(len(T)):
    pol_fit+=coef[i]*(samples-1960)**i
    
plt.plot(T,S_t,marker='*',color='red',linestyle=' ',markersize=10,label='Muestras')
plt.plot(samples,pol_fit,color='black',label='Vandermode')
plt.grid()
#plt.title(" Interpolación con Vandermode",fontsize=14)
#plt.title(r" Interpolación con  $(x-1925)^j$",fontsize=14)
plt.title(r" Interpolación con $(x-1960)^j$",fontsize=14)
plt.xlabel(" x",fontsize=14)
plt.ylabel(" y",fontsize=14)
plt.legend()
plt.show()

