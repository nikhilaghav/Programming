



class First
{

    public static void main(String A[])
    {
      
        System.out.println("Inside main");

        Arithmetic aobj= new Arithmetic(11,10);
        
        int Result=0;
        
        Result=aobj.Addition();

        System.out.println("Addition is : "+Result);

        Result =aobj.Subtraction();

        System.out.println("Subtraction is : "+Result);



    }
}

class Arithmetic
{
   public int No1,No2;

   public Arithmetic()
   {
    
     this.No1=0;
     this.No2=0;

   }
   public Arithmetic(int value1, int value2)
   {
    
     this.No1=value1;
     this.No2=value2;

   }
   
   public int Addition()
   {
      int Ans=0;
      Ans=this.No1 + this.No2;
      return Ans;

   }
    public int Subtraction()
   {
      int Ans=0;
      Ans=this.No1 - this.No2;
      return Ans;

   }


}
