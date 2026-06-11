class Program30
{
 public static void main(String args[])
 {
  Logic obj = new Logic();

  obj.CheckSign(-8);
 }

}

class Logic
{                  
 void CheckSign(int num)
 {
    if(num > 0)
    {
        System.out.println("Number is positive");
    }
    else if(num < 0)
    {
        System.out.println("Number is negative");
    }
    else
    {
        System.out.println("Number is zero");
    }
 }
}

