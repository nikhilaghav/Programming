#include<stdio.h>

int Factorial(int iNo)
{
  if(iNo < 0)
  {
    iNo= -iNo;
  }

  int iCnt=0;
  int iFact=1;

  for(iCnt = iNo; iCnt >=1; iCnt--)
  {
   iFact = iFact * iCnt;
  }
  return iFact;

  

}

int main()
{
 int iValue = 0,iRet = 0;

 printf("Enter number");
 scanf("%d",&iValue);

 iRet = Factorial(iValue);
 
 printf("Factorial of number is %d\n",iRet);

 return 0;
}

// Time complexity: O(N)