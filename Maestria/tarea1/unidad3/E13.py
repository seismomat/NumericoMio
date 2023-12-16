import numpy as np
import matplotlib.pyplot as plt
import math 

def biseccion(f,Tol,N,a,b):
    fa, fb = f(a), f(b)
    #no hay un cambio de signo (teorema del valor medio)
    #no existe raiz en el intervalo [a,b]
    if fa*fb>0:
        print ("no hay raiz en [a,b]")
        return
    #contador de iteraciones    
    n=1
    x0=0.0
    #mientras no se exceda el numero de iteraciones
    while n<=N:
        #se busca la raiz en el punto medio
        x1=(a+b)/2.0
        fx=f(x1)
        #en caso de que la iteracion siguiente y la diferencia
        #entre la iteracion anterior no excedan Tol, entonces
        #la iteracion actual se aproxima a la solucion buscada
        if abs(f(x1)) <= Tol and abs(x1-x0) <= Tol:
            return x1
        #en caso de no cumplir el criterio de tolerancia
        #se actualiza el rango de busqueda
        if (fa*fx <0.0):
            b=x1 
        if (fx*fa >0.0):      
            a=x1
        x0=x1
        #se incrementa el contador de iteraciones
        n=n+1



def f(x): 
  return x*math.cosh(50/x) -x -23

def df(x):
    return -(1/x)*math.sinh(50/x)+math.cosh(50/x)-1

raiz = biseccion(f,1e-8,1000,0.1,1)
print("La raíz con el método de la bisección es:", raiz)
