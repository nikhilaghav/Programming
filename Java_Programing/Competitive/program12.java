class Program32
{
 public static void main(String args[])
 {
  Logic obj = new Logic();

  obj.DisplayGrade(82);
 }

}

class Logic
{                  
 void DisplayGrade(int num)
 {
    if( num >=85  && num <= 100)
    {
        System.out.println("First class with distinction");
    }
    else if( num >= 75  && num < 85)
    {
        System.out.println("First class");
    }
    else if( num >= 55 && num < 75)
    {
        System.out.println("second class");
    }
    else if( num >= 35  && num < 55)
    {
        System.out.println("Pass class");
    }
    else if(num < 35)
    {
        System.out.println("Fail");
    }
    else
    {
        System.out.println("Invalid marks");
    }







 }
}

