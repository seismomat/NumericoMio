#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 22:12:35 2021

@author: mating
"""

import numpy as np 
from numpy import linalg as LA

import Tools_T3 as Ts

class Interpolation:
    def __init__(self,datas):
        self.data = datas['data']
        self.n=datas['n']    
        
    def Vandermode(self):
        M=np.zeros((self.data[0].shape[0],self.n+1))
        
        for i in range(self.n+1):
            M[:,i]=self.data[0]**i
            
        #print(M,"\t",self.data[1])
            
        return LA.solve(M,self.data[1])
        
    
    def CubicSplines(self):
        h=np.zeros(self.n);alpha=np.zeros(self.n+1);
        DC=np.zeros(self.n+1);DS=np.zeros(self.n);DI=np.zeros(self.n);
        c_j=np.zeros(self.n+1);b_j=np.zeros(self.n);d_j=np.zeros(self.n)
        
        h=self.data[0][1:]-self.data[0][0:-1]
        
        ## Compute the vector B
        for i in range(1,self.n):
            alpha[i]=(3/h[i])*(self.data[1][i+1]-self.data[1][i]) -\
            (3/h[i-1])*(self.data[1][i]-self.data[1][i-1])
            
        for i in range(1,self.n):
            DC[i]=2*(h[i-1]+h[i])
            DS[i-1]=h[i-1]
            DI[i]=h[i]
            
        DC[0]=1.0;DC[-1]=1.0
            
        c_j=Ts.Thomas(DC,DS,DI,alpha)
        
        for i in range(self.n):
            b_j[i]=(self.data[1][i+1]-self.data[1][i])*(1/h[i])-\
                (h[i]/3)*(c_j[i+1]+2*c_j[i])
                
            d_j[i]=(c_j[i+1]-c_j[i])/(3*h[i])
            
    
        return {'a_j':self.data[1][:-1],'b_j':b_j,'c_j':c_j[:-1],'d_j':d_j}
    
    def LinearSplines(self):
        A=np.ones((2,2));y=np.zeros(2);a_b=[]
        
        for i in range(self.data[0].shape[0]-1):
            A[0,0]=self.data[0][i];A[1,0]=self.data[0][i+1];
            y[0]=self.data[1][i];y[1]=self.data[1][i+1];
            
            
            a_b.append(LA.solve(A,y))
            # 0 index for slope
            # 1 index for intercept
        return a_b
    
    
    def Newton(self, punto):
        x=self.data[0]; y=self.data[1]
        coef=Ts.diferenciasDiv(x,y)
        # primer valor igual al termino independiente (revisar ejemplo)
        resultado = coef[0]
        # par de ciclos para evaluar el resto de los coeficientes
        for i in range(1, len(coef)):
            # siguiente coeficiente
            evaluacion = coef[i]
            # ciclo que evalua (x-xj)
            for j in range(i):
                evaluacion *= (punto-x[j])
            # se suma el resultado a lo ya calculado
            resultado += evaluacion
        # se devuelve el resultado
        return resultado
    
    def Lagrange(self, xi):
        # variable para almacenar el resultado
        result = 0.0
        f=self.data
        # longitud de los datos
        n = len(f[0])
        # ciclos para realizar la suma de multiplicaciones
        for i in range (n):
            # f(xi)=yi
            term = f[1][i]
            # for para calcular el coeficiente de Lagrange (Li)
            for j in range(n):
                # combinaciones en las que j!=i (revisar definicion de Li)
                if (j!=i):
                    # Li*f(xi)
                    term = (xi - f[0][j])/(f[0][i] - f[0][j])*term
            # se suma el Li*f(xi) con el resto de los valores evaluados
            result += term
        # se devuelve el resultado
        return result 

"""
#x=np.array([-1.0,0.0,2.0,5.0])
#y=np.array([6.0,1.0,3.0,66.0])

x=np.array([0.0,1.0,2.0,3.0])
y=np.exp(x)

#x=np.array([1.0,2.0,4.0])
#y=np.array([1.0,0.5,0.25])
x = [1.0,2.0,4.0,5.0,7.0]
y = [52.0,5.0,-5.0,-40.0,10.0]
datas={'data':(x,y),'n':3}

pol=Interpolation(datas)


print('Interpolacion en 3.0: ',pol.Newton( 3.0))
print("Interpolacion con Lagrange ",pol.Lagrange(3.0))


#se evalua el polinio (en forma de lista de coeficientes) en x=2
Ts.horner([1,-4,7,-5,-2], 2)
"""