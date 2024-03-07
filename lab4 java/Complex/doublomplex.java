public class doublomplex
{
    public static void main(String[] args)
   {

        Complex<Double> complex1 = new DoubleComplex(1.0, 2.0);
        Complex<Double> complex2 = new DoubleComplex(3.0, 4.0);

        Complex<Double> sum = complex1.add(complex2);
        Complex<Double> difference = complex1.subtract(complex2);
        Complex<Double> product = complex1.multiply(complex2);
        Complex<Double> quotient = complex1.division(complex2);

        
        System.out.println("Sum: " + sum.getReal() + " + " + sum.getImaginary() + "i");
        System.out.println("Difference: " + difference.getReal() + " + " + difference.getImaginary() + "i");
        System.out.println("Product: " + product.getReal() + " + " + product.getImaginary() + "i");
        System.out.println("Quotient: " + quotient.getReal() + " + " + quotient.getImaginary() + "i");
    }
       



}