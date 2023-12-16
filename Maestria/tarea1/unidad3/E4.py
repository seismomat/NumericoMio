import numpy as np
import matplotlib.pyplot as plt

def newton(f,df,Tol,N,x0):
    #contador de iteraciones
    n=1
    #mientras no se haya superado el limite de iteraciones
    while n<=N:
        #se evalua la funcion y su derivada
        fx=f(x0)
        dfx=df(x0)
        #se calcula la siguiente aproximacion
        xn = x0-(fx/float(dfx))
        #en caso de cumplir criterios se devuelve la raiz
        if abs(f(xn)) <= Tol and abs(xn-x0) <= Tol:
            print(" numero de iteraciones",n)
            return xn
        #actualizamos las aproximaciones
        x0 = xn
        #se incrementa el contador de iteraciones    
        n=n+1
    #raise Exception("Se alcanzo el maximo numero de iteraciones y no se encontro raiz")
    print("Se alcanzo el maximo numero de iteraciones y no se encontro raiz")

def fixPoint(f,Tol,N,x0):
    #contador de iteraciones
    n=1
    #mientras no se haya superado el limite de iteraciones
    while n<=N:
        #se evalua la funcion y su derivada
        fx=f(x0)
        #se calcula la siguiente aproximacion
        xn = fx
        #en caso de cumplir criterios se devuelve la raiz
        if abs(f(xn)-fx) <= Tol:
            print(" numero de iteraciones",n)
            return xn
        #actualizamos las aproximaciones
        x0 = xn
        #se incrementa el contador de iteraciones    
        n=n+1
    #raise Exception("Se alcanzo el maximo numero de iteraciones y no se encontro raiz")
    print("Se alcanzo el maximo numero de iteraciones y no se encontro raiz")

def df(x):
    return 2*x
def f(x):
  return (x**2)-3

def g1(x):
    return 3+x-(x**2)
def g2(x):
    return 1+x-((x**2)/3)

raiz = newton(f,df,10e-10,50,1)
print("La raíz con el método de Newton es:", raiz)
raiz = fixPoint(g2,10e-10,50,1)
print("La raíz con el método de Punto fijo:", raiz)
raiz = fixPoint(g1,10e-2,20,1)
print("La raíz con el método de Punto fijo es:", raiz)

