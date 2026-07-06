#include<stdio.h>

typedef unsigned int UINT;
typedef unsigned int BOOL;

#define TRUE 1
#define FALSE 0

BOOL ChkBit(UINT iNo, int iPos)
{
    UINT iMask = 1;
    UINT iAns = 0;

    iMask = iMask << iPos - 1;

    iAns = iNo & iMask;

    if(iAns == iMask)
    {
        return TRUE;
    }
    else
    {
        return FALSE;
    }
}

int main()
{
    UINT iValue = 0;
    UINT iPos = 0;
    BOOL bRet = FALSE;

    printf("Enetr number:");
    scanf("%u",&iValue);

    printf("Enetr position:");
    scanf("%u",&iPos);

    bRet = ChkBit(iValue,iPos);

    if(bRet == TRUE)
    {
        printf("Bit is ON\n");
    }
    else
    {
        printf("Bit is OFF\n");
    }

    return 0;
}