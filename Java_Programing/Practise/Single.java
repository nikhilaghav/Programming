 class Single 
{
    public static void main(String A[])
    {
        System.out.println("Inside main");

        Derived dobj=new Derived();

        System.out.println(dobj.i);
        System.out.println(dobj.j);
        System.out.println(dobj.x);

        dobj.fun();
        dobj.gun();


        System.out.println("End of main");



    }
}
 
 
  class Base
 {
   public int i,j;
    
   public Base()
   {
     System.out.println("Inside base constructor");
     this.i=0;
     this.j=0;
   }

   protected void finalize()
   {
     System.out.println("Inside finalize method of base");
   }
  
   public void fun()
   {
     System.out.println("Inside base fun");
   }


 }

 class Derived extends Base
 {
   public int x;

   public Derived()
   {
     System.out.println("Inside derived constructor");
     this.x=0;
   }

   protected void finalize()
   {
     System.out.println("Inside finalize of derived");
   }
   
   public void gun()
   {
    System.out.println("Inside gun of derived");
   }

 }

  
 
 
 
