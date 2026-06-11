class Program35
{
 public static void main(String args[])
 {
  Logic obj = new Logic();

  obj.CalculatePower(3,4);
 }

}

class Logic
{                  
 void CalculatePower(int base, int exp)
 {
   int iResult = 1;
   int iCnt = 0;

   for(iCnt = 0;iCnt < exp; iCnt++)
   {
     iResult = iResult * base;
   }

   System.out.println(iResult);

 }
}

