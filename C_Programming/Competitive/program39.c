#include<stdio.h>

double FhtoCs(float fTemp)
{
   double iCelsius;

   iCelsius = (fTemp - 32) * (5.0/9.0);

   return iCelsius;
}

int main()
{
 float fValue = 0.0f;
 double dRet = 0.0;

 printf("Enter temperature in Fahrenheit:");
 scanf("%f",&fValue);

 dRet = FhtoCs(fValue);

 printf("Temperature in celsius is: %lf \n",dRet);

 return 0;
}

// Time complexity:O(1)