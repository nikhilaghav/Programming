class Program42
{
 public static void main(String args[])
 {
  Logic obj = new Logic();

  obj.CountEvenOddRange(50);
 }

}

class Logic
{                  
 void CountEvenOddRange(int num)
 {
    int iDigit = 0, iCntEven = 0, iCntOdd = 0, iCnt = 0;
     
    for(iCnt = 1; iCnt < num; iCnt++)
    {
        if(iCnt % 2 == 0)
        {
            iCntEven++;
        }
        else
        {
            iCntOdd++;
        }
    }
    System.out.println("count of even numbers:"+iCntEven);
    System.out.println("count of odd numbers:"+iCntOdd);

 }
}

