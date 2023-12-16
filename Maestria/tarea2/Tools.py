import numpy as np
from numpy import linalg as LA
from numba import jit, float64,int64
from numba import njit, prange, set_num_threads
import numba as nb

import Tools2 as Ts2
#set_num_threads(4)

@jit(nogil=True,fastmath=True,nopython=True)
def Hfix(Haux,OM):
  """ Compute the HouseHolder matrix
        Inputs:
              Huax: float 2darray
              OM (Original Matrix): float 2darray
        Outputs:
              float 2darray

        >>>  OM=np.array([[0,1,1],[1,2,3],[1,1,1]])
            Haux=[[-0.16910198 -0.98559856]
            [-0.98559856  0.16910198]]
             Hfix(Haux,OM)
             >>>[[ 1.          0.          0.        ]
             [ 0.         -0.16910198 -0.98559856]
             [ 0.         -0.98559856  0.16910198]]
  """
  if Haux.shape==OM.shape:
    return Haux
  else:
    i=OM.shape[0]-Haux.shape[0]
    H=np.eye(OM.shape[0])
    for j in range(Haux.shape[0]):
      fil=j+i
      for k in range(Haux.shape[0]):
          col=k+i
          H[fil][col]=Haux[j][k]

    return H

@jit(nogil=True,fastmath=True,nopython=True)
def sign(x):
    """ Compute the sign function
    Inputs:
          x: float number

    Outputs:
          float number

    >>> sign(-5)
        -1
    """
    if x >= 0:
        return 1
    elif x < 0:
        return -1

def GivensMatrix(x,i,j):
    """ Compute the Givens rotations matrix
        Inputs:
              x: float array
              i: int number ( ith column,row)
              j: int number ( jth column,row)

        Outputs:
              float 2darray

        >>>  A=np.array([-1.0,2.0,3.0])
             GivensMatrix(A,0,1)
            [[-0.4472136   0.89442719  0.        ]
             [-0.89442719 -0.4472136   0.        ]
             [ 0.          0.          1.        ]]
    """
    vec=np.array([x[i], x[j]])
    rnorm=LA.norm(vec)
    c=vec[0]/rnorm;s=vec[1]/rnorm;
    Giv=np.eye(x.shape[0])
    Giv[i,i]=c; Giv[i,j]=s;
    Giv[j,j]=c;  Giv[j,i]=-s

    return Giv


def vectorDesign(x,arr,info):
    """ Compute the vector Design of a matrix design
            Inputs:
                  x: float number
                  arr: pased reference array
                  info: dictionary with the functional information

            Outputs:
                  arr: pased reference array

            >>>  vectorDesign(2,arr)
                [1   2  4  ]
    """
    if info['Functions'] == 'basics':
        for i in range(len(arr)):
            arr[i]=Ts2.Xi(x,i)

    elif info['Functions'] == 'exp':
        for i in range(len(arr)):
            arr[i]=Ts2.exp_i(x,info['weight'][i])

    elif info['Functions'] == 'Rational':
        for i in range(len(arr)):
            arr[i]=Ts2.Rational(x,info['weight'],i)

    elif info['Functions']=='loge':
        for i in range(len(arr)):
            arr[i]=Ts2.logXi(x,i)

    elif info['Functions']=='l1':
        for i in range(len(arr)):
            if i==0:
                arr[i]=1.0
            else:
                arr[i]=Ts2.l1(x)
    elif info['Functions']=='l2':
        for i in range(len(arr)):
            if i==0:
                arr[i]=1.0
            else:
                arr[i]=Ts2.l2(x)
    elif info['Functions']=='l3':
        for i in range(len(arr)):
            if i==0:
                arr[i]=1.0
            else:
                arr[i]=Ts2.l3(x)
    elif info['Functions']=='l4':
        for i in range(len(arr)):
            if i==0:
                arr[i]=1.0
            else:
                arr[i]=Ts2.l4(x)

def MatrixDesign(data,n,info):
    """ Compute the vector Design of a matrix design
            Inputs:
                data (): float number array
                n (polinomial grade): int number

            Outputs:
                DM (Design Matrix): 2d array float number

            >>> data=[[1],[2]]
             MatrixDesign(data,1,info)
                [[1 ,1 ],[1, 2]]
    """
    Datasize=data.shape[0]

    DM=np.zeros((Datasize,n+1))

    for element in range(Datasize):
        vectorDesign(data[element],DM[element],info)


    return DM

def Get_pol(coef,x):
    n=coef.shape[0]
    res=np.zeros_like(x)

    for i in range(n):
        res+= coef[i,0]*(x**i)

    return res

def Get_polLog(coef,x):
    n=coef.shape[0]
    res=np.zeros_like(x)


    """
    coef=np.flipud(coef)
    coef[1:]=np.exp(coef[1:])
    for i in range(n):
        res+= coef[i,0]*(np.log(x)**i)
    """
    if n==2:
        res=np.exp(coef[0,0])*(x**coef[1,0])
    elif n==3:
        res=np.exp(coef[0,0])*(x**coef[1,0])*(np.exp(coef[2,0]*(np.log(x)**2)))
    elif n==4:
        res=np.exp(coef[0,0])*(x**coef[1,0])*(np.exp(coef[2,0]*(np.log(x)**2)))*(np.exp(coef[3,0]*(np.log(x)**3)))

    return res

def sustDelante(L, b):
    n=len(L)
    y=np.empty_like(b)
    y[0] = b[0]/L[0][0]
    for i in range(1,n):
        y[i] = b[i]
        for j in range(0,i):
            y[i] -= L[i][j]*y[j]
        y[i] /= L[i][i]
    return y

def sustAtras(U, y):
    n=len(U)
    x=np.empty_like(y)
    x[n-1] = y[n-1]/U[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = y[i]
        for j in range(i+1,n):
            x[i] -= U[i][j]*x[j]
        x[i] /= U[i][i]
    return x

def get_residuals(data):
    res=[]
    for i in range(len(data[1])):
        aux=np.zeros(len(data[1][0]))
        for j in range(len(data[1][0])):
            aux[j]=LA.norm(data[0][j]-data[1][i][j])
        res.append(aux)

    return res

def get_residuals1D(data):
    res=[]
    for j in range(len(data[1])):
        res.append(LA.norm(data[0][j]-data[1][j]))
    return res

def get_residualsLog(data):
    res=[]
    coef=np.flipud(data[2])
    coef=np.exp(coef)
    if coef.shape[0]==2:
        for j in range(len(data[1])):
            res.append(LA.norm(data[0][j]-np.exp(coef[0])*(data[1][j]**coef[1]) ))
    elif coef.shape[0]==3:
        for j in range(len(data[1])):
            res.append(LA.norm(data[0][j]-np.exp(coef[0])*(data[1][j]**coef[1])*np.exp(coef[1]*(np.log(data[1][j])**2))  ) )

    return res
