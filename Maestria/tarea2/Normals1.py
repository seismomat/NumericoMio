import numpy as np
import math
from numpy import linalg as LA
import Tools as Ts
import sys
sys.path.append('/home/mating/Documents/numerical_analysis_master/programs/tarea1/unidad2')
from Sust import Sust
from invertion import Invertion
from NOSquareFacHouse import NOSquareFacHouse

class Normals:
    def __init__(self,data,n,info):
        self.M=data["M"]
        self.b=data["b"]
        self.n=n
        self.info=info
        self.Regression()
        self.condition=0.0

    def Regression(self):
        self.A=Ts.MatrixDesign(self.M,self.n,self.info)
        self.A=np.hstack((self.A,np.sin(self.M)))
        self.AT_A=self.A.T@self.A
        self.AT_b=self.A.T@self.b

    def SolveCholesky(self):
        method=Invertion(self.AT_A)
        L=method.Cholesky()
        self.condition=LA.cond(L,2)
        S=Sust(L,L.T,self.AT_b)
        x_g=S.get_Solve()

        return x_g
