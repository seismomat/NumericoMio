import numpy as np
import math
from numpy import linalg as LA
import Tools as Ts
import sys
sys.path.append('/home/mating/Documents/numerical_analysis_master/programs/tarea1/unidad2')
from Sust import Sust
from invertion import Invertion
from NOSquareFacHouse import NOSquareFacHouse

class NormalsConics:
    def __init__(self,data):
        self.x=data["x"]
        self.y=data["y"]
        self.b=self.x**2
        self.Regression()
        self.condition=0.0

    def Regression(self):
        self.A=np.hstack((self.y**2,self.x*self.y,self.x,self.y,np.ones_like(self.x)))
        self.AT_A=self.A.T@self.A
        self.AT_b=self.A.T@self.b

    def SolveCholesky(self):
        method=Invertion(self.AT_A)
        L=method.Cholesky()
        self.condition=LA.cond(L,2)
        S=Sust(L,L.T,self.AT_b)
        x_g=S.get_Solve()

        return x_g,self.A

    def SolveGrandSmith(self):
        method=Invertion(self.A)
        Q,R=method.QR()
        QT_A_b= Q.T@self.b
        x_g=Ts.sustAtras(R,QT_A_b)

        return x_g,self.A
