#include<stdio.h>

int CountDiff(int iNo)
{
 int iDigit=0;
 int iSumE=0;
 int iSumO=0;

 if(iNo < 0)
 {
    iNo = -iNo;
 }

 while(iNo > 0)
 {
    iDigit= iNo % 10;

    if(iDigit % 2 ==0)
    {
        iSumE = iSumE + iDigit;
    }
    else
    {
        iSumO = iSumO + iDigit;
    }
    
    iNo= iNo / 10;
 }
 return iSumE - iSumO;
}

int main()
{
 int iValue = 0;
 int iRet = 0;

 printf("Enter number");
 scanf("%d",&iValue);

 iRet = CountDiff(iValue);

 printf("%d",iRet);

 return 0;
}

// Time complexity: O(N)
// where N = number of digits