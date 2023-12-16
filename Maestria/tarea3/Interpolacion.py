#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 17:22:23 2021

@author: mating
"""

import numpy as np

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

''' Funcion que vevuelve la evaluacion de un valor
    x: conjunto de valores en el eje x
    coef: coeficientes del polinomio de Newton
    punto: valor en el cual se busca interpolar
    resultado: valor de la interpolacion en el valor xi
'''
def interpoladorNewton(x, coef, punto):
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


''' Interpolador de Lagrange
f: lista de datos (x0,y0),...,(xn,yn)
xi: punto en el que se evalua el polinomio
'''
def interpoladorLagrange(f, xi):
    # variable para almacenar el resultado
    result = 0.0
    # longitud de los datos
    n = len(f)
    # ciclos para realizar la suma de multiplicaciones
    for i in range (n):
        # f(xi)=yi
        term = f[i][1]
        # for para calcular el coeficiente de Lagrange (Li)
        for j in range(n):
            # combinaciones en las que j!=i (revisar definicion de Li)
            if (j!=i):
                # Li*f(xi)
                term = (xi - f[j][0])/(f[i][0] - f[j][0])*term
        # se suma el Li*f(xi) con el resto de los valores evaluados
        result += term
    # se devuelve el resultado
    return result 

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

#se evalua el polinio (en forma de lista de coeficientes) en x=2
horner([1,-4,7,-5,-2], 2)


# datos en la forma (x,y)
# x = (1.0,4.0,7.0)
# y = (52.0,-5.0,10.0)
# datos extendidos
x = (1.0,2.0,4.0,5.0,7.0)
y = (52.0,5.0,-5.0,-40.0,10.0)
# coeficientes (ai's) del polinomio de Newton
coef = diferenciasDiv(x,y)
# se muestran los coeficientes ai (diferencias divididas)
print(coef)
# resultado de la interpolacion en 3
print('Interpolacion en 3.0: ',interpoladorNewton(x, coef, 3.0))
f=((1.0,52.0),(2.0,5.0),(4.0,-5.0),(5.0,-40.0),(7.0,10.0))
print("Interpolacion con Lagrange ",interpoladorLagrange(f, 3.0))