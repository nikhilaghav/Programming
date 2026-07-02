#include<stdio.h>

int LastChar(char *str, char ch)
{
   int i = 0;
   int iPos = -1;

   while (str[i] != '\0')
   {
    if(str[i] == ch)
    {
       iPos = i;
    }
    i++;  
   }
   return iPos;
   
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

    iRet = LastChar(arr, cValue);

    if(iRet == -1)
    {
        printf("Character not found\n");
    }
    else
    {
        printf("Character location is:%d\n",iRet);
    }
    return 0;
}