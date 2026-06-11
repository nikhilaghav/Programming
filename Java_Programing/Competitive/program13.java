class Program33
{
 public static void main(String args[])
 {
  Logic obj = new Logic();

  obj.CheckDivisible(55);
 }

}

class Logic
{                  
 void CheckDivisible(int num)
 {
    if( (num % 5 ==0)  && (num % 11 == 0))
    {
        System.out.println("Number is divisible by 5 and 11");
    }
   
    else
    {
        System.out.println("number is not divisible");
    }

 }
}

