#include<stdio.h>

int RangeSumEven(int iStart , int iEnd)
{
  int iCount = 0;
  int iSum = 0;
  
  if(iStart < 0 || iEnd < 0 || iStart > iEnd)
  {
    return -1;
  }

  for(iCount =iStart; iCount <= iEnd; iCount++)
  {
    if(iCount % 2 == 0)
    {
        iSum = iSum + iCount;
    }
  }
  return iSum;
}

int main()
{
 int iValue1 = 0, iValue2 = 0, iRet =0;

 printf("Enter starting point:");
 scanf("%d",&iValue1);

 printf("Enter ending point:");
 scanf("%d",&iValue2);

 iRet = RangeSumEven(iValue1, iValue2);

 if(iRet ==-1)
 {
    printf("Invalid Range\n");
 }
 else
 {
 printf("Addition is %d\n",iRet);
 }

 return 0;
}

// Time complexity:O(N)
// where N=(iEnd - iStart + 1)