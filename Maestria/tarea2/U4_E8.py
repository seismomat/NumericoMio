import numpy as np
import NormalsConics as Ns
import matplotlib.pyplot as plt
from numpy import linalg as LA
def Get_conic():
    pass

x=np.array([1.02,0.95,0.87,0.77,0.67,0.56,0.44,0.30,0.16,0.01])
x=x.reshape((x.shape[0],1))
y=np.array([0.39,0.32,0.27,0.22,0.18,0.15,0.13,0.12,0.13,0.15])
y=y.reshape((y.shape[0],1))
data={'x':x,'y':y,'n':1}

pol=Ns.NormalsConics(data)
Fit_data,M=pol.SolveCholesky()

res=LA.norm(M@Fit_data-x**2)

print("Residual con Cholesky:",res)

Fit_data1,M1=pol.SolveGrandSmith()

res1=LA.norm(M1@Fit_data1-x**2)

print("Residual con Grand Smith:",res)
