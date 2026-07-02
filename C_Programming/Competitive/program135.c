#include<stdio.h>

void StrRevX(char *str)
{
    char *start = NULL;
    start = str;
    char temp ='\0';

    while( *str != '\0')
    {
        str++;
    }
    str--;
    
    while(str > start)
    {
        temp = *start;
        *start = *str;
        *str = temp;
        
        start++;
        str--;
    }

}

int main()
{
 char arr[20];

 printf("Enter string:");
 scanf("%[^'\n']s",arr);

 StrRevX(arr);

 printf("Modified string is %s\n",arr);

 return 0;
}