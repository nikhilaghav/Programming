#include<stdio.h>

int CountSmall(char *str)
{
  int icount = 0;

  while(*str != '\0')
 {
   if(*str >= 'a' && *str <= 'z')
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

  iRet = CountSmall(arr);

  printf("frequency is:%d\n",iRet);

  return 0;
}