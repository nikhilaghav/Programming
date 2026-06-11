//Accept number from user and check whether number is even or odd.

# include<stdio.h>

# define true 1
# define false 0
typedef int BOOL;

BOOL ChkEven(int iNo)
{
  if(iNo % 2 == 0)
  {
    return true;
  }
  else
  {
    return false;
  }

}
int main()
{
  int iValue = 0;
  BOOL bRet = false;

  printf("Enter number");
  scanf("%d" ,&iValue);

  bRet = ChkEven(iValue);

  if(bRet==true)
  {
    printf("Number is even\n");
  }
  else
  {
    printf("Number is odd \n");
  }


  return 0;
}