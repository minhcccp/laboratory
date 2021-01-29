public class Main {
  public static int persistence(long n) {
    int prod = 1;

    for (char digit : String.valueOf(n).toCharArray()) {
      prod *= Character.getNumericValue(digit);
    }

    return (n <= 9 ? 0 : persistence(prod) + 1);
  }

  public static void main(String[] args) {
    System.out.println(persistence(99));
  }
}


