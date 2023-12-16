#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:56:31 2021

@author: mating
"""
import Cuadraturas as Int 
import sympy as sp
import numpy as np

def funcion(x):
	return (1/np.sqrt(2))*np.exp(-(x**2)/2)

def main():
    print('Integral de cuadratura simple')
    print(Int.rectangulos(funcion,0,1,100))
    print('Integral de cuadratura punto medio')
    print(Int.PuntoMedio(funcion,0,1,100))
    print('Integral de cuadratura Trapecio')
    print(Int.Trapecio(funcion,0,1))
    print('Integral de cuadratura TrapecioCompuesto')
    print(Int.TrapecioCompuesto(funcion,0,1,100))
    print('Simpson 1/3')
    print(Int.Simpson1_3(funcion,0,1))
    print('Simpson 3/3')
    print(Int.Simpson3_8(funcion,0,1))
    print('Cuadratura Gaussian')
    print(Int.CuaGauss(funcion,0,1))
    
    x = sp.Symbol('x')
    Inte=sp.integrate((1/sp.sqrt(2))*sp.exp(-x**2/2), (x, 0, 1)).evalf()
    print(" El valor analítico de la integral es: ",Inte)
main()