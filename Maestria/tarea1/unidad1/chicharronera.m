% programa que calcula la formula general de segundo grado 

clear all;
clc
% coeficientes de la formula general de segundo grado 
a=1; b= -(1e11+1e-11);c=1;


radical= sqrt(b^2-4*a*c) % discriminante

n1= -b + radical % numerador de la primer raiz
n2= -b - radical % denominador de la segunda raiz

x1= n1/(2*a) % primer raiz
x2= n2/(2*a) % segunda raiz 

disp(' Resultados con radicalizacion')

x1 

x3= (2*c)/(-b+radical)


