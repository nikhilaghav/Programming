class Program27
{
 public static void main(String args[])
 {
  Logic obj = new Logic();

  obj.PrintEvenNumbers(20);
 }

}

class Logic
{                  
 void PrintEvenNumbers(int num)
 {
    int iCnt =0;

    for(iCnt = 0; iCnt <= num; iCnt++)
    {
        if(iCnt % 2 == 0)
        {
            System.out.println(iCnt);
        }
    }   
 }
}

