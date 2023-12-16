#include<iostream>
#include<vector>
#include <functional>
#include <cstdlib>

using namespace std;

class SolvNoLinearEq{

	public:
		int N; // max iterations
		double Tol; // minimum tolerance


	SolvNoLinearEq(int imax, double t){
		N=imax;
		Tol=t;
	}

	double bisection(double a, double b,function<double(double)> func){
		double fa,fb,x1,x0=0.0,fx;
		int n=1;

		fa=func(a);
		fb=func(b);

		if(fa*fb>0){
			cout<<"There is no root in [a,b]"<<endl;
			return 0.0;
		}

		while(n<=N){

	        x1=(a+b)/2.0;
	        fx=func(x1);
	        if (abs(func(x1)) <= Tol && abs(x1-x0) <= Tol) {
	        	cout<<" el numero de iteraciones Biseccion :"<<n<<endl;
	        	return x1;
	        }

	        if (fa*fx <0.0) b=x1; 
	        if (fx*fa >0.0) a=x1;

	        x0=x1;
	        n+=1;
		}
	}

	double FalsePosition(double a, double b,function<double(double)> func){
		double fa,fb,x1,x0=0.0,fx;
		int n=1;

		fa=func(a);
		fb=func(b);

		if(fa*fb>0){
			cout<<"There is no root in [a,b]"<<endl;
			return 0.0;
		}

		while(n<=N){
			fa=func(a);
			fb=func(b);
	        x1=(a*fb-b*fa)/(fb-fa);
	        fx=func(x1);
	        if (abs(func(x1)) <= Tol && abs(x1-x0) <= Tol){
	        	cout<<" el numero de iteraciones Falsa posicion :"<<n<<endl;
	        	return x1;
	        }

	        if (fa*fx <0.0) b=x1; 
	        if (fx*fa >0.0) a=x1;

	        x0=x1;
	        n+=1;
		}
	}

	/// 
	double Secant(double a, double b,function<double(double)> func){
		double fa,fb,xn;
		int n=1;

		while(n<=N){
			fa=func(a);
			fb=func(b);
	        xn=  b-fb*( (b-a)/( (double) (fb-fa) ) );

	        if (abs(func(xn)) <= Tol && abs(b-a) <= Tol)
	        {
	        	cout<<" el numero de iteraciones secante :"<<n<<endl;
	        	 return xn;
	        	}

	        a=b; 
	        b=xn;
	        n+=1;
		}
	}

	///
	double Newton(double x0,function<double(double)> func,function<double(double)> dfunc){
		double fx,dfx,xn;
		int n=1;

		while(n<=N){
			fx=func(x0);
			dfx=dfunc(x0);
	        xn= x0- (fx/dfx);
	        if (abs(func(xn)) <= Tol && abs(xn-x0) <= Tol)
	        {
	        	cout<<" el numero de iteraciones Newton :"<<n<<endl;
	        	 return xn;
	        }

	        x0=xn;
	        n+=1;
		}

		cout<<"We dont find roots"<<endl;
	}


};

