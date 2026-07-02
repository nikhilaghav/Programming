#include<stdio.h>

void DisplayASCII()
{
  int i = 0;
  printf("symbol\tdecimal\thexadecimal\toctal\n");

  for(i = 0; i<=255; i++)
  {
    printf("%c\t%d\t\t%X\t%o\n",i,i,i,i);
  }
}

int main()
{
 DisplayASCII();
 
 return 0;
}