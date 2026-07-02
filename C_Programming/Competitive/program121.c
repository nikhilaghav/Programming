#include<stdio.h>

int CountCapital(char *str)
{
  int iCnt = 0;
  int icount = 0;

  while(*str != '\0')
 {
   if(*str >= 'A' && *str <= 'Z')
   {
     icount++;
   }
   str++;
 }

 return icount;
}

int main()
{
  char arr[20];
  int iRet = 0;

  printf("Enter string:");
  scanf("%[^\n]s",arr);

  iRet = CountCapital(arr);

  printf("frequency of capital is:%d\n",iRet);

  return 0;
}