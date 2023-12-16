#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 22:03:47 2021

@author: mating
"""
import numpy as np 
from numpy import linalg as LA
import matplotlib.pyplot as plt 

import Tools_T3 as Ts
from Interpolation import Interpolation

x = [-1.0,0.0,2.0,5.0]
y = [6.0,1.0,3.0,66.0]

#x = [1.0,2.0,4.0]
#y = [1.0,3.0,3.0]

coef= Ts.diferenciasDiv(x,y)

print(" Coeficientes obtenidos con diferencias divididas \n")
print(coef)
coef=np.flip(coef)
# se muestran los coeficientes ai (diferencias divididas)

print("\n")
print(" Evaluación con Horner \n")
Ts.horner(coef, -1.0)

datas={'data':(x,y),'n':3}

pol=Interpolation(datas)

z=np.linspace(-2,6,100); f_z=[]
for i in z:
    f_z.append(pol.Newton( i))
    
plt.plot(z,f_z,color='black')
plt.plot(x,y,marker='*',color='red',linestyle=' ',markersize=10)
plt.grid()
plt.title(" Interpolación ",fontsize=14)
plt.xlabel(" x",fontsize=14)
plt.ylabel(" y",fontsize=14)
plt.show()

print(" Diferencias divididas \n")
print(Ts.TabladifDiv(x,y))
