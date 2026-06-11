class Program37
{
 public static void main(String args[])
 {
  Logic obj = new Logic();

  obj.PrintReverse(10);
 }

}

class Logic
{                  
 void PrintReverse(int n)
 {
   int iCnt = 0;

   for(iCnt = n; iCnt > 0; iCnt--)
   {
    System.out.println(iCnt);
    
   }
   
 }
}

