#include<stdio.h>

void MultipleDisplay(int iNo)
{
  int iCnt=0;
  iCnt=1;
  while(iCnt<=5)
  { 
    printf(" %d ",iNo*iCnt);

    iCnt++;
  }
  printf("\n");
}

int main()
{
 int iValue = 0;

 printf("Enter number:");
 scanf("%d",&iValue);

 MultipleDisplay(iValue);

 return 0;
}

// Time Complexuty:O(1)