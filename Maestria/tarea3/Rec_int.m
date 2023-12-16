function [integrl] = Rec_int(n,f)

    if n==0
        integrl=integral(f,0,1);
    else 
        integrl=(1/n)-5*Rec_int(n-1,f);
    end 
    
end

