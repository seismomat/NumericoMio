clear all; clc;

data.k=1:16;
data.x=10.^-data.k;
data.f_expx=(exp(data.x)-1)./data.x;
data.f_logx=(exp(data.x)-1)./log(exp(data.x));

fprintf(" k=15")
fprintf(" exp= %f \t log= %f \n",data.f_expx(15),data.f_logx(15))

fprintf(" k=16")
fprintf(" exp= %f \t log= %f \n",data.f_expx(16),data.f_logx(16))