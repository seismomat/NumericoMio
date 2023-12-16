import numpy as np
from numpy import linalg as LA
import Normals as Ns
import Normals1 as Ns1
import Graphic2 as Gr
import Tools as Ts

def LinearRegression(datas):
    information=datas['information']
    settings=datas['settings']
    t=datas['t']
    y=datas['y']

    M=np.vstack(t)
    b = np.vstack(y)
    data={"M":M, "b":b}
    t=np.array(t); y=np.array(y); y_g=[];
    cond=[]

    pol=Ns.Normals(data,1,information)
    Fit_data=pol.SolveCholesky()
    y_g=Ts.Get_pol(Fit_data,t)

    Res=Ts.get_residuals1D((y,y_g))
    info={'Data':(t,y), 'Fit':(t,y_g),'settings':settings,'Res':Res}
    pt=Gr.Graphic2(info)

    return Res

def LinearRegression1(datas):
    information=datas['information']
    settings=datas['settings']
    t=datas['t']
    y=datas['y']

    M=np.vstack(t)
    b = np.vstack(y)
    data={"M":M, "b":b}
    t=np.array(t); y=np.array(y); y_g=[];
    cond=[]

    pol=Ns1.Normals(data,1,information)
    Fit_data=pol.SolveCholesky()
    y_g=Fit_data[0]+Fit_data[1]*t+Fit_data[2]*np.sin(t)

    Res=Ts.get_residuals1D((y,y_g))
    info={'Data':(t,y), 'Fit':(t,y_g),'settings':settings,'Res':Res}
    pt=Gr.Graphic2(info)

    return Res

def LinearRegressionS(datas):
    information=datas['information']
    settings=datas['settings']
    t=datas['t']
    y=datas['y']

    M=np.vstack(t)
    b = np.vstack(y)
    data={"M":M, "b":b}
    t=np.array(t); y=np.array(y); y_g=[];
    cond=[]

    pol=Ns.Normals(data,1,information)
    Fit_data=pol.SolveCholesky()
    y_g=Ts.Get_pol(Fit_data,t)

    Res=Ts.get_residuals1D((y,y_g))


    return Res,y_g
