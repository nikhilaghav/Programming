#include<stdio.h>

void Number(int iNo)
{
 if(iNo <= 50)
 {
    printf("small");
 }
 else if(iNo > 50 && iNo <= 100)
 {
    printf("medium");
 }
 else
 {
    printf("large");

 }

 printf("\n");
}

int main()
{
 int iValue = 0;

 printf("Enter number:");
 scanf("%d",&iValue);

 Number(iValue);

 return 0;
}

// Time complexity:O(1)