import numpy as np
from numpy import linalg as LA

class EigenNewton:
    def __init__(self,data):
        self.A=data['A']
        self.x0=data['x0']
        self.l0=data['l0']
        self.n=data['n']
        self.I=np.eye(self.A.shape[0])

    def EigenN(self):

        self.xk=self.x0
        self.lk=self.l0

        m=0
        while m<self.n:
            self.A_lk_I= self.A -self.lk*self.I
            self.A_xk_lk_xk= self.A@self.xk -self.lk*self.xk

            J_f_1=np.hstack((self.A_lk_I,-self.xk))
            J_f_2=np.hstack((2*self.xk.T,np.zeros((1,1))))

            self.J_f= np.vstack((J_f_1,J_f_2))

            self.b=np.vstack((self.A_xk_lk_xk,self.xk.T@self.xk -1))

            self.sk_dk=LA.solve(self.J_f,self.b)

            self.xk_1= self.xk - self.sk_dk[:-1]
            self.lk_1= self.lk - self.sk_dk[-1]

            self.xk=self.xk_1
            self.lk=self.lk_1

            m+=1

        return self.xk,self.lk[0][0]
