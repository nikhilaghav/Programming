class Program41
{
 public static void main(String args[])
 {
  Logic obj = new Logic();

  obj.ProductOfDigits(234);
 }

}

class Logic
{                  
 void ProductOfDigits(int num)
 {
    int iDigit = 0, iMult = 1, iCnt = 0;

    while(num > 0)
    {
        iDigit = num % 10;
        
        iMult = iMult * iDigit;
        
        num = num / 10;
    }
    System.out.println(iMult );
 }
}

