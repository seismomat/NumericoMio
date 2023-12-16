import numpy as np
from numpy import linalg as LA

"""
This module contains the basis functions for the Regression code
"""
Xi=lambda x,n : x**n

logXi=lambda x,n :(np.log(x))**n

exp_i= lambda x,L: np.exp(-L*x)

def Rational(x,alphas,n):
    phi_j_x= 0.0
    for alpha in range(len(alphas)):
        phi_j_x+= alphas[alpha]*(x**alpha)

    return  phi_j_x

def l1(x):
    if x>28 :
        return 0
    elif x>=20 and x<=28:
        return (-1/28)*x+1

def l2(x):
    if x>=20 and x<=28:
        return (1/8)*(x-20)
    elif x>28 and x<=39:
        return (-1/11)*(x-28)+1
    elif x>39:
        return 0

def l3(x):
    if x>=20 and x<=28:
        return 0
    elif x>28 and x<=39:
        return (1/11)*(x-28)
    elif x>39:
        return (-1/6)*(x-39)+1

def l4(x):
    if x<=39:
        return 0
    elif x>39:
        return (1/6)*(x-39)
