import numpy as np
from numpy import linalg as LA
import Normals as Ns
import Graphic as Gr
import Tools as Ts

t=[0, 4, 7.5, 25, 31, 48.75, 52, 58.5, 72.7, 78, 95, 96, 108, 112, 133, 136.75, 143, 156.5, 166.7, 181]
y = [8, 6, 6, 7, 8, 10, 13, 18, 33, 38, 76, 78, 164, 175, 280, 300, 320, 405, 385, 450]

#t=[1.0,2.0,3.0,4.0]
#y=[6.0,5.0,7.0,10.0]

M=np.vstack(t)
b = np.vstack(y)
data={"M":M, "b":b}
t=np.array(t); y=np.array(y); y_g=[]; grades=np.arange(1,6)
information={"Functions":'basics',"weight":'null'}

#pol=Ns.Normals(data,1,information)
#Fit_data=pol.SolveHouseHolder()

cond=[]
for grade in grades:
    pol=Ns.Normals(data,grade,information)
    Fit_data=pol.SolveHouseHolder()
    cond.append(pol.get_conditionHouseHolder())
    y_g.append( Ts.Get_pol(Fit_data,t))

Res=Ts.get_residuals((y,y_g))
settings={'titulo':'Regresión lineal con ecuaciones normales',
'x':'Tiempo [seg]','y': 'Evolución de bacterias','grades':grades}
info={'Data':(t,y), 'Fit':(t,y_g),'settings':settings,'Res':Res}

pt=Gr.Graphic(info)
pt.plotCond((grades,np.array(cond),'yes'))
