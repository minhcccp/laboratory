import java.util.Arrays;
import java.util.stream.Collectors;

public class Main {
  public static int persistence(long n) {
    int result = 0;

    while (n >= 10) {
      result++;

      int prod = 1;

      for (char digit : String.valueOf(n).toCharArray()) {
        prod *= Character.getNumericValue(digit);
      }

      n = prod;
    }

    return result;
  }

  public static void main(String[] args) {
    System.out.println();
  }
}


