#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 20:03:08 2021

@author: mating
"""
import numpy as np 
import matplotlib.pyplot as plt 

from Interpolation import Interpolation

x = [-1.0,0.0,2.0,5.0]
y = [6.0,1.0,3.0,66.0]



datas={'data':(x,y),'n':3}

pol=Interpolation(datas)

z=np.linspace(-2,6,100); f_z=[]
for i in z:
    f_z.append(pol.Lagrange( i))
    
plt.plot(z,f_z,color='black')
plt.plot(x,y,marker='*',color='red',linestyle=' ',markersize=10)
plt.grid()
plt.title(" Interpolación de Lagrange",fontsize=14)
plt.xlabel(" x",fontsize=14)
plt.ylabel(" y",fontsize=14)
plt.show()

