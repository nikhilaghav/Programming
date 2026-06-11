#include<stdio.h>

# define PI 3.14

double CircleArea(float fRadius)
{
    return PI * fRadius * fRadius;
}

int main()
{
 float fValue = 0.0f;
 double dRet = 0.0;

 printf("Enter radius:");
 scanf("%f",&fValue);

 dRet = CircleArea(fValue);

 printf("Area of circle is %lf\n",dRet);

 return 0;
}

// Time complexity:O(1)