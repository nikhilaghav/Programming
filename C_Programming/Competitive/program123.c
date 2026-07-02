#include<stdio.h>

int Difference(char *str)
{
  int icountcap = 0, icountsmall= 0;

  while(*str != '\0')
 {
   if(*str >= 'a' && *str <= 'z')
   {
     icountsmall++;
   }
   else if(*str >= 'A' && *str <= 'Z')
   {
    icountcap++;
   }
   str++;
 }

 return icountsmall - icountcap;
}

int main()
{
  char arr[20];
  int iRet = 0;

  printf("Enter string:");
  scanf("%[^\n]s",arr);

  iRet = Difference(arr);

  printf("%d\n",iRet);

  return 0;
}