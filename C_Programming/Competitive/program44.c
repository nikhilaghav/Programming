#include<stdio.h>

int MultDigits(int iNo)
{
 int iDigit=0;
 int iMult=1;

 if(iNo < 0)
 {
    printf("Enter positive number \n");
 }

 while(iNo > 0)
 {
    iDigit= iNo % 10;

    iMult = iMult * iDigit;
    
    iNo= iNo /10;
 }
 return iMult;
}

int main()
{
 int iValue = 0;
 int iRet = 0;

 printf("Enter number:");
 scanf("%d",&iValue);

 iRet = MultDigits(iValue);

 printf("%d",iRet);

 return 0;
}

// Time complexity: O(N)
// where N = number of digits