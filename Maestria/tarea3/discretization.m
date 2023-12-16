function [Discret]= discretization (Discret)

   
    Discret.d1(1)=Discret.a;
    
    for i=2:length(Discret.d1)
        Discret.d1(i)=round(Discret.d1(i-1)+Discret.h,Discret.red);
    end  
    
    for k=1:length(Discret.d2)
        Discret.d2(k)= round(Discret.a+(k-1)*Discret.h ,Discret.red);
        
    end
    
end 


