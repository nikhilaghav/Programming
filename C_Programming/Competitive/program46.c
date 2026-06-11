#include<stdio.h>

void RangeDisplay(int iStart , int iEnd)
{
   int iCount =0;

   if(iStart > iEnd)
   {
    printf("Invalid Range");
   }

   for(iCount= iStart; iCount <= iEnd; iCount++)
   {
    printf(" %d ",iCount);
   }

   printf("\n");
}

int main()
{
 int iValue1 = 0, iValue2 = 0;

 printf("Enter starting point:");
 scanf("%d",&iValue1);

 printf("Enter ending point:");
 scanf("%d",&iValue2);

 RangeDisplay(iValue1, iValue2);

 return 0;
}

// Time complexity:O(N)
// where N=(iEnd - iStart + 1)