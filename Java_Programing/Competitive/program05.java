class Program
{
 public static void main(String args[])
 {
  Logic obj = new Logic();
  
  obj.PrintTable(5);
}

}

class Logic
{
 void PrintTable(int num)
 {
    int iCnt = 0;

    for(iCnt = 1; iCnt <= 10; iCnt++)
    {
        System.out.println(num * iCnt);
    }
  
 }
}

