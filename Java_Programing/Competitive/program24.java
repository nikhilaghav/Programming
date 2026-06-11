class Program44 
{
 public static void main(String args[])
 {
  Logic obj = new Logic();

  obj.CountFactors(20);
 }

}

class Logic
{                  
 void CountFactors(int num)
 {
    int  iCnt = 0, iCount = 0;
     
    for(iCnt = 1; iCnt <= num/2; iCnt++)
    {
        if(num % iCnt == 0)
        {
            iCount++;
        }
    }
    System.out.println(iCount);
 }
}

