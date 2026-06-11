class Program26
{
 public static void main(String args[])
 {
  Logic obj = new Logic();

  obj.CheckPrime(11);
}

}

class Logic
{                  
 void CheckPrime(int num)
 {
    int iCnt = 0;
    boolean bflag = true;

    for(iCnt = 2; iCnt < (num / 2); iCnt++)
    {
        if(num % iCnt == 0)
        {
            bflag = false;
            break;
        }
    }
    if(bflag ==true)
    {
        System.out.println("It is a prime number");
    }
    else
    {
        System.out.println("It is not prime");
    }
  
 }
}

