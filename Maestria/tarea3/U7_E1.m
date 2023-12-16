clear all; clc;

Discret.a=5; 
Discret.b=15; 
Discret.n=21;
Discret.red=2;
Discret.h=(Discret.b-Discret.a)/Discret.n;
Discret.d1=zeros(1,Discret.n+1);
Discret.d2=zeros(1,Discret.n+1);
Discret= discretization (Discret); 

%% discretizaciones 
for i=1:length(Discret.d1)
    fprintf(" %f \t %f \n",Discret.d1(i),Discret.d2(i))
end 

%% Diferencias entre discretizaciones
for i=1:length(Discret.d1)-1
    fprintf("%f \t %f \t %f \n",Discret.h,(Discret.d1(i+1)-Discret.d1(i)),(Discret.d2(i+1)-Discret.d2(i)))
end 
