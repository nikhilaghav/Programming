class program21
{
 public static void main(String args[])
 {
  Logic obj = new Logic();
 
  obj.sumOfDigits(1234);
  
 }

}

class Logic
{
 void sumOfDigits(int num)
 {
    int iDigit = 0, iSum = 0;
    
    while(num > 0)
    {
        iDigit = num % 10;
        iSum = iSum + iDigit;
        num = num /10;

    }
    System.out.println("Sum of digits is:"+iSum);
 }
}

