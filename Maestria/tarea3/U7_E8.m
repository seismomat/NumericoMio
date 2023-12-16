%n=input('ingrese n ');
data.n=63;
data.t=linspace(0,2*pi,data.n+2);
data.h=data.t(2)-data.t(1)
data.SolE=10*cos(4*data.t);

c=data.h^2;
b=16*c-2;

A = diag(b*ones(1,data.n)) + diag(ones(1,data.n-1),1) + diag(ones(1,data.n-1),-1);
F=zeros(1,data.n);
F(1)=-10;
F(data.n)=-10;

data.SolN=A\F';


plot(data.t(1:data.n),data.SolN)
hold on
plot(data.t,data.SolE)
legend('Solucion Numerica','Solucion Exacta')
grid()
title(' Solución del oscilador armónico')
xlabel('Tiempo [segundos]')
ylabel(' x(t) ')