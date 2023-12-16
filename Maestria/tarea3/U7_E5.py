#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:31:16 2021

@author: mating
"""
import Cuadraturas as Int 
import sympy as sp

def funcion(x):
	return x**2-3*x-5

def main():
    print('Integral de cuadratura simple')
    print(Int.rectangulos(funcion,2, 3,100))
    print('Integral de cuadratura punto medio')
    print(Int.PuntoMedio(funcion,2, 3,100))
    print('Integral de cuadratura Trapecio')
    print(Int.Trapecio(funcion,2, 3))
    print('Integral de cuadratura TrapecioCompuesto')
    print(Int.TrapecioCompuesto(funcion,2, 3,100))
    print('Simpson 1/3')
    print(Int.Simpson1_3(funcion,2, 3))
    print('Simpson 3/3')
    print(Int.Simpson3_8(funcion,2, 3))
    print('Cuadratura Gaussian')
    print(Int.CuaGauss(funcion,2, 3))
    
    x = sp.Symbol('x')
    print(" El valor analítico de la integral es: ",sp.integrate(x**2-3*x-5, (x, 2, 3)).evalf())
main()