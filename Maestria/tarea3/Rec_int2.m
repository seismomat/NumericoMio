function [integrl] = Rec_int2(n,f,i)

    if n==i
        integrl=integral(f,0,1);
    else 
        integrl=(1/(5*(i+1)))-(1/5)*Rec_int(i+1,f);
    end 
    
end


