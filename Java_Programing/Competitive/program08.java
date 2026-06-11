class Program28
{
 public static void main(String args[])
 {
  Logic obj = new Logic();

  obj.PrintOddNumbers(20);
 }

}

class Logic
{                  
 void PrintOddNumbers(int num)
 {
    int iCnt =0;

    for(iCnt = 0; iCnt <= num; iCnt++)
    {
        if(iCnt % 2 != 0)
        {
            System.out.println(iCnt);
        }
    }   
 }
}

