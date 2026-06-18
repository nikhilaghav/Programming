#include<iostream>
using namespace std;

class Demo
{
   public:
    int i;
   private:
    int j;
   protected:
     int k;
   
   public:
     Demo()
     {
       i=0;
       j=0;
       k=0;

     }

     void Display()
     {
         cout<<"value of i:"<<i<<"\n";
         cout<<"value of j:"<<j<<"\n";
         cout<<"value of k:"<<k<<"\n";
         
     }

};

int main()
{
    Demo dobj;

    dobj.Display();

         cout<<"value of i:"<<dobj.i<<"\n";
         cout<<"value of j:"<<dobj.j<<"\n";
         cout<<"value of k:"<<dobj.k<<"\n";
         



    return 0;
}