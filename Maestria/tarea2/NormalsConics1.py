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
        self.z=data["z"]
        self.b=-self.x**2-self.y**2-self.z**2
        self.Regression()
        self.condition=0.0

    def Regression(self):
        self.A=np.hstack((-2*self.x,-2*self.y,-2*self.z,np.ones_like(self.x)))
        self.AT_A=self.A.T@self.A
        self.AT_b=self.A.T@self.b

    def Solve(self):
        self.x_g=LA.solve(self.AT_A,self.AT_b)
        r_g=np.sqrt(abs(self.x_g[0]**2+self.x_g[1]**2+self.x_g[2]**2-self.x_g[3]**2))
        return self.x_g,r_g

    def SolveHouseHolder(self):
        Fac=NOSquareFacHouse(self.A)
        rank=LA.matrix_rank(self.A)
        if rank== self.A.shape[1]:
            Q,R=Fac.HouseHolder()
            self.condition=LA.cond(Q,2)
            QT_A_b= Q.T@self.b
            self.x_g=Ts.sustAtras(R[:rank],QT_A_b[:rank])

        r_g=np.sqrt(abs(self.x_g[0]+self.x_g[1]+self.x_g[2]-self.x_g[3]))
        return self.x_g,r_g

    def get_matrix(self):
        self.Ma=np.hstack(((self.x-self.x_g[0])**2,(self.y-self.x_g[1])**2,(self.z-self.x_g[2])**2))

        return self.Ma
