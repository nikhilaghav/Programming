#include<stdio.h>

void TableRev(int iNo)
{
  if(iNo < 0)
  {
    iNo = -iNo;
  }

  int iCnt = 0;

  for(iCnt=10; iCnt >= 1; iCnt--)
  {
    printf(" %d ", iNo * iCnt);
  }
  printf("\n");
  
}

int main()
{
 int iValue = 0;

 printf("Enter Number:");
 scanf("%d",&iValue);

 TableRev(iValue);

 return 0;
}