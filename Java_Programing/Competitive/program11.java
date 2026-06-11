class Program31
{
 public static void main(String args[])
 {
  Logic obj = new Logic();

  obj.CheckLeapYear(2024);
 }

}

class Logic
{                  
 void CheckLeapYear(int num)
 {
    if((num % 400 == 0) || ((num % 4 == 0) && ( num % 100 != 0)))
    {
        System.out.println("Year is leap ...");
    }
    else
    {
        System.out.println("Year is not leap..");
    }
 }
}

