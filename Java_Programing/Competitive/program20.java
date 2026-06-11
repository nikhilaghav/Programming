class Program40
{
 public static void main(String args[])
 {
  Logic obj = new Logic();

  obj.FindSmallestDigit(89535);
 }

}

class Logic
{                  
 void FindSmallestDigit(int num)
 {
    int iDigit = 0,iMin = 9;

    while(num > 0)
    {
        iDigit = num % 10;

        if(iDigit < iMin)
        {
            iMin = iDigit;
        }
        num = num / 10;
    }
    System.out.println(iMin);
 }
}

