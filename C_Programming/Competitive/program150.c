#include <stdio.h>

typedef int BOOL;
typedef unsigned int UINT;

#define TRUE 1
#define FALSE 0 

UINT OnBit(UINT iNo)
{
    UINT iMask = 0xF;

    iNo =  iNo | iMask;

    return iNo;
}

int main()
{
    UINT iValue = 0;
    UINT Ret = 0;

    printf("Enter number:");
    scanf("%u",&iValue);

    Ret = OnBit(iValue);

    printf("updated number is:%u\n",Ret);

    return 0;
}