
using LinearAlgebra

function Aleatorian_initial(A)
	n=4
	Id=Matrix{Float64}(I, n, n)

	X=rand(n,n)
	println(X)
	println()

	for i=0:5
		X= X +X*(Id-A*X)
	end 

	println(inv(A))
	println()
	println(X)

end 

function determinate_initial(A)
	n=4
	Id=Matrix{Float64}(I, n, n)

	value=norm(A,1)*norm(A,Inf)
	X=(1/value).*A'
	println(X)
	println()

	for i=0:20
		X= X +X*(Id-A*X)
	end 

	println(inv(A))
	println()
	println(X)

end 

M= [2.0 5.0 6.0 8.0; -7.0 5.0 6.0 4.0; -1.0 2.0 3.0 5.0; 0.0 2.0 8.0 9.0]

#Aleatorian_initial(M)
determinate_initial(M)