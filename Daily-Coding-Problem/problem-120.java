public class Service {
   private static Service instanceOne = null;
   private static Service instanceTwo = null;

   private static int calls = 0;

   private Service() {
      // Disallow creation through the constructor
   }

   public static Service getInstance() {
      if(instanceOne == null) {
         instanceOne = new Service();
         instanceTwo = new Service();
      }

      if (calls++ % 2 == 0) {
        return instanceOne;
      }
      return instanceTwo;
   }
}
