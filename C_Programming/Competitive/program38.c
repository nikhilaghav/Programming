#include<stdio.h>

int KMtoMeter(int iNo)
{
  return iNo * 1000;
}

int main()
{
 int iValue = 0, iRet = 0;

 printf("Enter distance:");
 scanf("%d",&iValue);

 iRet = KMtoMeter(iValue);

 printf("Distance in meter is %d", iRet);

 return 0;
}
// Time complexity:O(1)