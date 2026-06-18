#include<iostream>
using namespace std;



int main()
{

   int no=11;

   int &x=no;

   cout<<"value of no:"<<no<<"\n";  //11
   cout<<"value of x:"<<x<<"\n";    //11

   cout<<"address of no:"<<&no<<"\n"; //100
   cout<<"address of x:"<<&x<<"\n";   //100

  cout<<"size  of no: "<<sizeof(no)<<"\n"; //4
  cout<<"size  of x: "<<sizeof(x)<<"\n";  //4
   


    return 0;
}