class Demo
{
   public int i;
   private int j;
   protected int k;
   
   public Demo()
   {
     i=0;
     j=0;
     k=0;
     
   }

   public void display()
   {
      
      System.out.println("value of i:" +i);  //allowed
      System.out.println("value of j:" +j);  //allowed
      System.out.println("value of k:" +k);  //allowed
    
   }

}


class Access
{

        {

             Demo dobj= new Demo();

             dobj.display();

             System.out.println("value of i:" +dobj.i);  //
             System.out.println("value of j:" +dobj.j);
             System.out.println("value of k:" +dobj.k);
    
        }
     
}