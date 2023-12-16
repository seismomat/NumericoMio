import numpy as np
import scipy.linalg
from numpy import linalg as LA
import Tools as Ts
import sys
sys.path.append('/home/mating/Documents/numerical_analysis_master/programs/tarea1/unidad2')
from Sust import Sust
from invertion import Invertion
from NOSquareFacHouse import NOSquareFacHouse
from FactGivens import FactGivens

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
        self.AT_A=self.A.T@self.A
        self.AT_b=self.A.T@self.b

    def SolveCholesky(self):
        method=Invertion(self.AT_A)
        L=method.Cholesky()
        self.condition=LA.cond(L,2)
        S=Sust(L,L.T,self.AT_b)
        x_g=S.get_Solve()

        return x_g

    def SolveHouseHolder(self):
        Fac=NOSquareFacHouse(self.A)
        rank=LA.matrix_rank(self.A)
        if rank== self.A.shape[1]:
            Q,R=Fac.HouseHolder()
            self.condition=LA.cond(R,2)
            QT_A_b= Q.T@self.b
            x_g=Ts.sustAtras(R[:rank],QT_A_b[:rank])

        return x_g

    def SolveGivens(self):
        Fac=FactGivens(self.A)
        rank=LA.matrix_rank(self.A)
        if rank== self.A.shape[1]:
            R,Q=Fac.Givens()
            self.condition=LA.cond(R,2)
            QT_A_b= Q.T@self.b
            x_g=Ts.sustAtras(R[:rank],QT_A_b[:rank])

        return x_g

    def SolveLU(self):
        P, L, U = scipy.linalg.lu(self.AT_A)
        y_g=Ts.sustDelante(L,self.AT_b)
        x_g=Ts.sustAtras(U,y_g)
        return x_g

    def get_conditionHouseHolder(self):
        return self.condition

    def get_conditionCholesky(self):
        return self.condition
