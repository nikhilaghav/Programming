class Program43
{
 public static void main(String args[])
 {
  Logic obj = new Logic();

  obj.DisplayFactors(12);
 }

}

class Logic
{                  
 void DisplayFactors(int num)
 {
    int  iCnt = 0;
     
    for(iCnt = 1; iCnt <= num/2; iCnt++)
    {
        if(num % iCnt == 0)
        {
            System.out.println(iCnt);
        }
    }
 }
}

