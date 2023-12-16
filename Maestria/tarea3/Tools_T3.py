#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 17:29:14 2021

@author: mating
"""
import numpy as np 

def Thomas(d0,d1,d2,b):
    # d0 principal, d2 inferior, d1 superior, b sol
	n=d0.shape[0]
	x=np.zeros(n)

	for i in range(n-1):
		a=0.0
		a=d1[i]/d0[i]
		d0[i+1]=d0[i+1]-a*d2[i]
		b[i+1]=b[i+1]-a*b[i]
	
	x=susAtrasDF(d0,d2,b,x)
	return x

# sustitucion hacia atras 
def susAtrasDF(d0,d2,b,x):
    n=d0.shape[0]
    x[n-1]=b[n-1]/d0[n-1]
	
    for i in range(n-2,-1,-1):
        x[i]=(b[i]-d2[i]*x[i+1])/d0[i]
    return x

''' Algoritmo que implementa el polinomio de Newton
    x: conjunto de valores en el eje x
    f: conjunto de valores en el eje y
    F[0]: coeficientes del polinomio de Newton
'''
def diferenciasDiv(x,f):
    #generamos la matriz de diferencias divididas
    F = np.zeros((len(x),len(x)))
    #la primer columna siempre son los valores de y
    for i in range(len(x)):
        F[i][0] = f[i]
    #se calcula la columna j, tomado como base la columna previa
    for j in range(1,len(x)):
        for i in range(len(x)-j):
            #se deja fija la columna y se desplaza sobre los renglones
            F[i][j] = (F[i+1][j-1]-F[i][j-1])/(x[i+j]-x[i])
    return F[0]

''' Algoritmo que implementa el polinomio de Newton
    x: conjunto de valores en el eje x
    f: conjunto de valores en el eje y
    F[0]: coeficientes del polinomio de Newton
'''
def TabladifDiv(x,f):
    #generamos la matriz de diferencias divididas
    F = np.zeros((len(x),len(x)))
    #la primer columna siempre son los valores de y
    for i in range(len(x)):
        F[i][0] = f[i]
    #se calcula la columna j, tomado como base la columna previa
    for j in range(1,len(x)):
        for i in range(len(x)-j):
            #se deja fija la columna y se desplaza sobre los renglones
            F[i][j] = (F[i+1][j-1]-F[i][j-1])/(x[i+j]-x[i])
      
    for i in range(1,len(x)):
        F[:,i]=np.flip(F[:,i])
        F[i:,i]=np.flip(F[i:,i])
    return F
'''Algoritmo de Horner para evaluar polinomios
coef: lista de coeficientes comenzando de izquierda
a derecha por el de mayor grado
x: valor en el cual se quiere evaluar el polinomio
'''
def horner(coef, x):
    # el primer valor es igual al coeficiente mas grande
    p = coef[0]
    # comenzamos en 1 ya que el primer coeficiente se asigna antes
    # de ingresar al ciclo for
    for i in range(1,len(coef)):
        # se calcula el resto de los valores como se describe en
        # en algoritmo
        p = coef[i]+x*p
    print(p)