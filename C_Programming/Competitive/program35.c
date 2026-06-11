#include<stdio.h>

int FactorialDiff(int iNo)
{
 if(iNo < 0)
 {
    iNo = -iNo;
 }

 int iCnt=0;
 int iMult=1;
 int iMultX=1;

 for(iCnt = iNo; iCnt >= 1; iCnt--)
 {
    if(iCnt % 2 == 0)
    {
        iMult=iMult * iCnt;
    }
 }

 for(iCnt = iNo; iCnt >= 1; iCnt--)
 {
    if(iCnt % 2 != 0)
    {
        iMultX=iMultX * iCnt;
    }
 }
 
 return iMult - iMultX;

}  


int main()
{
 int iValue = 0,iRet = 0;

 printf("Enter number");
 scanf("%d",&iValue);

 iRet = FactorialDiff(iValue);

 printf(" Factorial difference  is %d \n",iRet);

 return 0;
}

// Time complexity: O(2N)