x= pi/4;
h=1; 
n=1;

error_delante=zeros(20)
error_c=zeros(20)
aches=zeros(20)

while(n<=20)
    global h=h/10;
	fx_h=sin(x+h);
	ffx_h=sin(x-h);
	fx=sin(x);
	der= (fx_h-fx)/h;
	der_c= (fx_h-ffx_h)/(2*h);

	println(" iteracion ",n)
	println("h ",h," sin(x+h) ",fx_h," sin(x) ",fx, "\n")
	println(" derivada ",der," cos(x) ",cos(x),"\n")
	println(" der centrada ", der_c, "\n")
	println(" error hacia delante= ", abs(der -cos(x)))
	println(" error centrada= ", abs(der_c -cos(x)))
	
	global error_delante[n]=abs(der -cos(x));
	global error_c[n]=abs(der_c -cos(x));
	global aches[n]=h;
	global n+=1;

end 

println(length(aches))
using PyPlot

scatter(aches,error_delante,label="Error esquema hacia delante")
scatter(aches,error_c,label="Error esquema centrado")
title("Error en estimación de la derivada")
xlim([0.1e-20,0.2])
ylim([0.001,1])
xscale("log")
yscale("log")
xlabel(" h ")
ylabel(" error absoluto")
grid()
legend()

show()