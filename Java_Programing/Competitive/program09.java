class Program29
{
 public static void main(String args[])
 {
  Logic obj = new Logic();

  obj.SumEvenOddDigits(123456);
 }

}

class Logic
{                  
 void SumEvenOddDigits(int num)
 {
    int iDigit = 0 , iSumEven = 0,iSumOdd = 0;
    
    while(num > 0)
    {
     iDigit = num % 10;
     
     if(iDigit % 2 == 0)
     {
        iSumEven = iSumEven + iDigit;
     }
     else
     {
        iSumOdd = iSumOdd + iDigit;
     }
     num = num / 10;
    }  
    System.out.println("Sum of even digits is "+iSumEven);
    System.out.println("Sum of odd digits is "+iSumOdd);
 }
}

