 public class DoubleComplex implements Complex<Double> {

    private double realNumber;
    private double imaginaryNumber;

    
    public DoubleComplex(double real, double imaginary) {
        realNumber = real;
        imaginaryNumber = imaginary;
    }
    
   
    public Double getReal() {
        return realNumber;
    }

    
    public Double getImaginary() {
        return imaginaryNumber;
    }

    
    public Complex<Double> add(Complex<Double> z) {
        return new DoubleComplex(realNumber + z.getReal(), imaginaryNumber + z.getImaginary());
    }

    
    public Complex<Double> subtract(Complex<Double> z) {
        return new DoubleComplex(realNumber - z.getReal(), imaginaryNumber - z.getImaginary());
    }

    
    public Complex<Double> multiply(Complex<Double> z) {
        double resultReal = realNumber * z.getReal() - imaginaryNumber * z.getImaginary();
        double resultImaginary = realNumber * z.getImaginary() + imaginaryNumber * z.getReal();
        return new DoubleComplex(resultReal, resultImaginary);
    }

    @Override
    public Complex<Double> division(Complex<Double> z) {
        double denominator = z.getReal() * z.getReal() + z.getImaginary() * z.getImaginary();
        double resultReal = (realNumber * z.getReal() + imaginaryNumber * z.getImaginary()) / denominator;
        double resultImaginary = (imaginaryNumber * z.getReal() - realNumber * z.getImaginary()) / denominator;
        return new DoubleComplex(resultReal, resultImaginary);
    }
} 
