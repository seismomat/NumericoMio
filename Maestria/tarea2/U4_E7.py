import numpy as np
from numpy import linalg as LA
import pandas as pd

import sys
sys.path.append('/home/mating/Documents/numerical_analysis_master/programs/tarea1/unidad2')

from invertion import Invertion
from NOSquareFacHouse import NOSquareFacHouse
from FactGivens import FactGivens

norm_Giv=[];norm_House=[];norm_Smith=[];epss=[];
Id=np.eye(3)

indices=np.arange(0,16)
for i in indices:
    A=np.ones((3,3))
    eps=10**(-float(i))
    epss.append(eps)
    A[1,0]+=eps
    A[0,2]+=eps
    A[2,1]+=eps

    method=Invertion(A)
    Q_Smith,R_smith=method.QR()

    norm_Smith.append(LA.norm(Q_Smith@Q_Smith.T - Id))
    Fac=NOSquareFacHouse(A)
    Q_House,R_House=Fac.HouseHolder()
    norm_House.append(LA.norm(Q_House@Q_House.T - Id))
    Fac=FactGivens(A)
    R_Giv,Q_Giv=Fac.Givens()
    norm_Giv.append(LA.norm(Q_Giv@Q_Giv.T - Id))

dic={'n':indices,'eps':epss,'Grand Smith':norm_Smith,'HouseHolder':norm_House,'Givens':norm_Giv}

Df=pd.DataFrame(dic)

print(Df)
