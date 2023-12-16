#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:46:21 2021

@author: mating
"""
import Cuadraturas as Int 
import sympy as sp

def f(x,y):
	return 8*x-10*y+2

def main():

    Integral=Int.CuaGauss2D(f,1,2,-1,1)
    print('Valor de la integral con Cuadratura Gaussiana: ', Integral)
    
    x = sp.Symbol('x')
    y=sp.Symbol('y')
    I1=sp.integrate(8*x-10*y+2, (y, -1, 1))
    inte=sp.integrate(I1,(x, 1, 2)).evalf()
    print(" El valor analítico de la integral es: ",inte)
main()