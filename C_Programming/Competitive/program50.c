#include<stdio.h>

int RangeDisplayReverse(int iStart , int iEnd)
{
  int iCount = 0;
  int iSum = 0;
  
  if(iStart > iEnd)
  {
    printf("Invalid range");
  }

  for(iCount =iEnd; iCount >= iStart; iCount--)
  {
    printf(" %d ",iCount);
  }
  printf("\n");
  
}

int main()
{
 int iValue1 = 0, iValue2 = 0, iRet =0;

 printf("Enter starting point:");
 scanf("%d",&iValue1);

 printf("Enter ending point:");
 scanf("%d",&iValue2);

 RangeDisplayReverse(iValue1, iValue2);

 return 0;
}

// Time complexity:O(N)
// where N=(iEnd - iStart + 1)