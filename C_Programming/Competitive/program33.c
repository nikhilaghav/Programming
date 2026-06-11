#include<stdio.h>

int EvenFactorial(int iNo)
{
 if(iNo < 0)
 {
    iNo = -iNo;
 }

 int iCnt=0;
 int iMult=1;

 for(iCnt = iNo; iCnt >= 1; iCnt--)
 {
    if(iCnt % 2 == 0)
    {
        iMult=iMult * iCnt;
    }
 }
 return iMult;
}

int main()
{
 int iValue = 0,iRet = 0;

 printf("Enter number");
 scanf("%d",&iValue);

 iRet = EvenFactorial(iValue);

 printf("Even Factorial of number is %d",iRet);

 return 0;
}

// Time complexity: O(N)