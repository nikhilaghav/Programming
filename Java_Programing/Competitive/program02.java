class program22
{
 public static void main(String args[])
 {
   Logic obj = new Logic();
   
   obj.checkPalindrome(121);
 }
 }

class Logic
{
 void checkPalindrome(int num)
 {
   int iDigit = 0,iRev = 0;
   int itemp =0;

   itemp = num;
   
   while(num > 0)
   {
    iDigit = num % 10;
    iRev = (iRev * 10) + iDigit;
    num = num / 10;
   }
   if(itemp == iRev)
   {
    System.out.println(" IT is a palindrome");
   }
   else
   {
    System.out.println("It is not palindrome");
   }

 }
}

