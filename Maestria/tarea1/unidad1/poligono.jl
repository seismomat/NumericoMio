p= 2*sqrt(2);

p1=zeros(58);
for n=3:60
	global p1[n-2]=p
	radical1= sqrt(1-(p/(2^n))^2 )
	radical2= sqrt(2*(1-radical1))
	global p=radical2*(2^n)
	
end 

p2=zeros(58);
rn=2/(2+sqrt(2));
p=0;p=rn;

for n=3:60
	global p2[n-2]=p
	global rn= rn/ (2 + sqrt(4-rn))
	global p=sqrt(rn)*(2^n)
	
end 

iter=3:60
using PyPlot

scatter(iter,p1,label="Sin radicalizar")
scatter(iter,p2,label="radicalizada")
title("Error en algoritmo del poligono")
grid()
legend()
xlabel("Iteraciones")
ylabel(" Valor de la raíz")
show()