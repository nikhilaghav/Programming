#include<stdio.h>

double RectArea(float fWidth, float fHeight)
{
  return fWidth * fHeight;
}

int main()
{
 float fValue1 = 0.0f, fValue2 = 0.0f;
 double dRet = 0.0;

 printf("Enter width:");
 scanf("%f",&fValue1);

 printf("Enter height:");
 scanf("%f",&fValue2);

 dRet = RectArea(fValue1, fValue2);

 printf("Area is:%lf",dRet);

 return 0;
}

// Time complexity:O(1)