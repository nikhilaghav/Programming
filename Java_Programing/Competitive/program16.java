class Program36
{
 public static void main(String args[])
 {
  Logic obj = new Logic();

  obj.SumEvenNumbers(10);
 }

}

class Logic
{                  
 void SumEvenNumbers(int n)
 {
   int iCnt = 0, iSum = 0;

   for(iCnt = 1; iCnt <= n; iCnt++)
   {
    if(iCnt % 2 == 0)
    {
        iSum = iSum + iCnt;
    }
   }
   System.out.println(iSum);

 }
}

