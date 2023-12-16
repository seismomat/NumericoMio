import numpy as np
from numpy import linalg as LA
import Normals as Ns
import Graphic as Gr
import Tools as Ts

W=[0.017,0.087,0.174,1.110,1.740,4.090,5.450,5.960,0.025,0.111
,0.211,0.999,3.020,4.280,4.580,4.680,0.020,0.085,0.171,1.290,3.040
,4.290,5.300,0.020,0.119,0.210,1.320,3.340,5.480,0.025,0.233,0.783
,1.350,1.690,2.750,4.830,5.530]

W=sorted(W)
R=[0.154,0.296,0.363,0.531,2.230,3.580,3.520,2.400,0.23,0.357,0.366,0.771,2.010
,3.280,2.960,5.100,0.181,0.260,0.334,0.870,3.590,3.400,3.880,0.180,0.299,0.428
,1.150,2.830,4.150,0.234,0.537,1.470,2.480,1.440,1.840,4.660,6.940]

R=sorted(R)

M=np.vstack(np.log(W))
b = np.vstack(np.log(R))
data={"M":M, "b":b}
W=np.array(W); R=np.array(R); R_g=[]; grades=np.arange(1,4)
information={"Functions":'basics',"weight":'null'}

#pol=Ns.Normals(data,1,information)
#Fit_data=pol.SolveHouseHolder()

cond=[];Res=[]
for grade in grades:
    pol=Ns.Normals(data,grade,information)
    Fit_data=pol.SolveCholesky()
    R_g.append( Ts.Get_polLog(Fit_data,W))

Res=Ts.get_residuals((W,R_g))
#Res.append(Ts.get_residualsLog((R,W,Fit_data)))
settings={'titulo':'Regresión lineal con ecuaciones normales',
'x':'Consumo de oxígeno [seg]','y': 'Peso de las larvas','grades':grades}
info={'Data':(W,R), 'Fit':(W,R_g),'settings':settings,'Res':Res}

pt=Gr.Graphic(info)
#pt.plotCond((grades,np.array(cond),'no'))
