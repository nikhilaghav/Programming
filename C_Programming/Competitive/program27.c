#include<stdio.h>

void Display(int iNo)
{
    if(iNo < 0)
    {
        iNo = -iNo;
    }

    switch (iNo)
    {
    case 0:printf("Zero");
           break;
    
    case 1:printf("one");
           break;

    case 2:printf("Two");
           break;

    case 3:printf("Three");
           break;

    case 4:printf("Four");
           break;

    case 5:printf("five");
           break;

    case 6:printf("six");
           break;

    case 7:printf("seven");
           break;

    case 8:printf("eight");
           break;

    case 9:printf("nine");
           break;

    default:printf("Invalid number");
            
    }
 
}

int main()
{
 int iValue = 0;

 printf("Enter number:");
 scanf("%d",&iValue);

 Display(iValue);

 return 0;
}

//Time complexity:O(1)