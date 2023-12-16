import numpy as np
from numpy import linalg as LA

import EigenNewton as EN
import EigenPot as EP

A=np.random.rand(3,3)
#A= np.array([[0.0,1.0,-1.0],[1.0,1.0,0.0],[-1.0,0.0,1.0]])
x0=np.array([1/np.sqrt(2),1/np.sqrt(2),0.0]).reshape((A.shape[0],1))
l0= x0.T@(A@x0)

data={'A':A,'x0':x0,'l0':l0,'n':100}
EiNew= EN.EigenNewton(data)
EiPot=EP.EigenPot(data)

xk,lk=EiNew.EigenN()
xk1,lk1=EiPot.EigenPow()

print("Matriz inicial\n")
print(A)
print("\n")
print("Eigenvector con método de Newton \n", xk)
print("Eigenvector con método de la Potencia \n", xk1)
print()
print("Eigenvalor con método de Newton ",lk)
print("Eigenvalor con método de la Potencia  ",lk1)

W,V=LA.eig(A)
print("Eigenvalores con método de numpy \n",W)
print()
print("Eigenvectores con método de numpy \n",V)
