#include<stdio.h>

typedef unsigned int UINT;


UINT ONBit(UINT iNo, int iPos)
{
    UINT iMask = 1;

    iMask = iMask << (iPos - 1);

    iNo = iNo | iMask;

    return iNo;
}

int main()
{
    UINT iValue = 0;
    UINT iPos = 0;
    UINT Ret = 0;

    printf("Enetr number:");
    scanf("%u",&iValue);

    printf("Enetr position:");
    scanf("%u",&iPos);

    Ret = ONBit(iValue,iPos);

    printf("Modified number is:%u\n",Ret);
    return 0;
}