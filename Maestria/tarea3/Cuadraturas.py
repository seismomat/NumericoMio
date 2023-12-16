#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 16:50:16 2021

@author: mating
"""
import numpy as np 

def Trapecio(f,a,b):
 
    return ((b-a)/2)*(f(a)+f(b))

def TrapecioCompuesto(f,a,b,n): 
    x=np.linspace(a,b,n+1)

    # formula del trapecio compuesto
    cuadratura=0.0
    for i in range (1,len(x)-1):
        cuadratura+=f( x[i])

    integral=((b-a)/(2*n))*(2*cuadratura+f(a)+f(b))
    return integral
    
def PuntoMedio(f,a,b,n):
	# a punto inicial del intervalo 
	# b punto final del intervalo 
	# f funcion a integrar
	# n los puntos que se usaran para integrar 
	
	x=np.linspace(a,b,n) # se crea la particion
	cuadratura=0.0
	for i in range (len(x)-1):
		cuadratura+=f( (x[i]+x[i+1])/2 )
		
	integral=((b-a)/n)*cuadratura

	return integral 

def rectangulos(f,a,b,n):
	# a punto inicial del intervalo 
	# b punto final del intervalo 
	# f funcion a integrar
	# n los puntos que se usaran para integrar 
	
	x=np.linspace(a,b,n) # se crea la particion
	cuadratura=0.0
	for i in range (len(x)):
		cuadratura+=f(x[i])
		
	integral=((b-a)/n)*cuadratura

	return integral 

def Simpson1_3(f,a,b):

    h=(b-a)/2
    x1=a+h

        
    return (h/3)*(f(a)+4*f(x1)+f(b))


def Simpson3_8(f,a,b):

    h=(b-a)/3
    x1=a+h
    x2=a+2*h

        
    return (3/8)*h*(f(a)+3*f(x1)+3*f(x2)+f(b))
    
def CuaGauss(f,a,b):
    x=np.array([0.774,0.0,-0.774])
    # pesos de Gauss
    c=np.array([0.556,0.889,0.556])

    # acumulador
    cuadratura=0.0
    # constante de 
    dx=(b-a)/2
    # por cada punto de integracion
    for i in range(len(x)):
        # nuevo punto de integracion
        changeVar=0.0
        changeVar=(((b-a)*x[i])+b+a)/2
        # se acumula la evualuacion de f en nuevo punto
        cuadratura+=c[i]*f(changeVar)
        
    return cuadratura*dx
    

def CuaGauss2D(f,a,b,d1,d):
    x=np.array([0.774,0.0,-0.774])
    # pesos de Gauss
    c=np.array([0.556,0.889,0.556])

    # acumulador
    cuadratura=0.0
    # constante de 
    dx=(b-a)/2
    dy=(d-d1)/2
    # por cada punto de integracion
    for i in range(len(x)):
        for j in range(len(x)):
            # nuevo punto de integracion
            changeVar=0.0
            changeVar=(((b-a)*x[i])+b+a)/2
            changeVar1=0.0
            changeVar1=(((d-d1)*x[j])+d+d1)/2
            # se acumula la evualuacion de f en nuevo punto
    
            cuadratura+=c[i]*c[j]*f(changeVar,changeVar1)
            
    return cuadratura*dx*dy