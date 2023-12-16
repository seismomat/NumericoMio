#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 23:16:13 2021

@author: mating
"""

import numpy as np 
import matplotlib.pyplot as plt 

from Interpolation import Interpolation

x=np.linspace(-1.0,1.0,100)

f=lambda xx:1/(1+25*xx**2)

fx=f(x)
n=np.arange(5,25,5)

for j in n:
    nodos=np.linspace(-1.0,1.0,j)
    fnodos=f(nodos)
    
    
    datas={'data':(nodos,fnodos),'n':3}
    
    pol=Interpolation(datas)
    
    f_z=[]
    for i in x:
        f_z.append(pol.Newton( i))
        
    
    plt.plot(x,f_z,label='n='+str(j))
plt.plot(x,fx,color='black',label='funcion de Runge')
#plt.plot(nodos,fnodos,marker='*',color='red',linestyle=' ',markersize=10)
plt.grid()
plt.title(" Interpolación con Newton",fontsize=14)
plt.xlabel(" x",fontsize=14)
plt.ylabel(" y",fontsize=14)
plt.legend()
plt.show()


"""
En esta sección se resuelve la interpolacion con los nodos de
Chebyshev
"""
for j in n:
    xi_nodos=np.zeros(j)
    for i in range(1,j+1):
        xi_nodos[i-1]=np.cos(((2*i-1)*np.pi)/(2*j))
        
    fxi_nodos=f(xi_nodos)    
    datas={'data':(xi_nodos,fxi_nodos),'n':3}
    
    pol=Interpolation(datas)
    
    f_z=[]
    for i in x:
        f_z.append(pol.Newton( i))
        
    
    plt.plot(x,f_z,label='n='+str(j))
plt.plot(x,fx,color='black',label='funcion de Runge')
#plt.plot(nodos,fnodos,marker='*',color='red',linestyle=' ',markersize=10)
plt.grid()
plt.title(" Interpolación con nodos de Chebyshev",fontsize=14)
plt.xlabel(" x",fontsize=14)
plt.ylabel(" y",fontsize=14)
plt.legend()
plt.show()

