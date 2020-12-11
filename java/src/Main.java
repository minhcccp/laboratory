import java.io.IOException;

public class Main {
  /**
   * Iterate through each line of input.
   */
  public static void main(String[] args) throws IOException {
    reverseSpell("And now          this:");
  }

  public static void reverseSpell(String input) {
    String result = "";

    for (int i = 0; i < input.length(); i++) {
      char currentChar = Character.toLowerCase(input.charAt(i));
      if (Character.isDigit(currentChar) || Character.isLetter(currentChar)) {
        result = String.valueOf(currentChar) + (i > 0 ? "-" : "") + result;
      }
    }
    System.out.println(result);
  }
}
