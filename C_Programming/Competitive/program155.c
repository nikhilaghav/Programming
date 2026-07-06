#include<stdio.h>

typedef unsigned int UINT;

UINT ToggleBit(UINT iNo)
{
    UINT iMask1 =0xf000000f;
    
    iNo = iNo ^ iMask1;

    return iNo;
}

int main()
{
    UINT iValue = 0;
    UINT Ret = 0;

    printf("Enetr number:");
    scanf("%u",&iValue);

    Ret = ToggleBit(iValue);

    printf("Modified number is:%u\n",Ret);
    return 0;
}