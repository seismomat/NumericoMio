clear all;clc;
n=50;

myfun = @(x) (x.^n)./(x+5);
f = @(x) 1./(x+5);
q = quad(myfun,0,1);
y0=integral(f,0,1);

%%% iterativo 
for i=1:n
    y=(1/i)-5*y0;
    y0=y;
end 

fprintf(' ------ Primer esquema  --------- \n' )
fprintf('y n = 1/n −5 yn−1 ,  \n' )
fprintf("Iterativo: Valor aproximado %f / valor real %f \n",y0,q)

%%%% Recursividad 

 y0= Rec_int(n,f);
 fprintf("Recursivo: Valor aproximado %f / valor real %f \n",y0,q)
 
 fprintf(' ----  Segundo  esquema ----- \n' )
 fprintf('y n-1 = 1/5n - 1/5 yn ,  \n' )
 
 %%% iterativo 
 yn= quad(myfun,0,1);
for i=n:-1:1
    y=(1/(5*i))-(1/5)*yn;
    yn=y;
end 

fprintf("Iterativo: Valor aproximado %f / valor real %f \n",yn,quad(f,0,1))

%%%% Recursividad 

 yn= Rec_int2(n,myfun,0);
  fprintf("Recursivo: Valor aproximado %f / valor real %f \n",yn,quad(f,0,1))
