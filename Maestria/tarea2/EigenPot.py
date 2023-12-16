import numpy as np
from numpy import linalg as LA

class EigenPot:
    def __init__(self,data):
        self.A=data['A']
        self.x0=data['x0']
        self.l0=data['l0']
        self.n=data['n']
        self.I=np.eye(self.A.shape[0])

    def EigenPow(self):

        self.xk=self.x0
        self.lk=self.l0

        m=0
        while m<self.n:
            self.w=self.A@self.xk
            self.xk_1= self.w/LA.norm(self.w)
            self.lk_1= self.xk_1.T @ self.A @ self.xk_1

            self.xk=self.xk_1
            self.lk=self.lk_1[0][0]

            m+=1

        return self.xk,self.lk
