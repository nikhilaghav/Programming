#include<stdio.h>

int FirstChar(char *str, char ch)
{
   int i = '\0';

   while (str[i] != '\0')
   {
    if(str[i] == ch)
    {
        return i;
    }
    i++;  
   }
   return -1;
   
}

int main()
{
    char arr[20];
    char cValue = '\0';
    int iRet = 0;

    printf("Enter string:");
    scanf("%[^\n]s",arr);

    printf("Enter the character:");
    scanf(" %c",&cValue);

    iRet = FirstChar(arr, cValue);

    printf("Character location is:%d\n",iRet);

    return 0;
}