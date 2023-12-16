#include<iostream>
#include<vector>
#include <functional>
#include <cstdlib>
#include <math.h>
#include "/home/mating/Documents/numerical_analysis_master/programs/dotHfiles/SolvNoLinearEq.h"

using namespace std;


double f(double x){
  //return (x*x)-1.0;
  return x-exp(-x);

}

double df(double x){
  //return 2.0*x;
  return 1+exp(-x);
}

int main(){

	double root,root1,root2,root3;

	SolvNoLinearEq solver(1000,10E-8);
	root=solver.bisection(0,2.0,f);
	root1=solver.FalsePosition(0,2.0,f);
	root2=solver.Secant(0,2.0,f);
	root3=solver.Newton(0.5,f,df);

	cout<<"the root is "<<root<<endl;
	cout<<"the root is "<<root1<<endl;
	cout<<"the root is "<<root2<<endl;
	cout<<"the root is "<<root3<<endl;

	return 0;
}