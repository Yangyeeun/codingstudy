import java.util.*;
import java.lang.String;

public class num2675 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int total = s.nextInt();

        for (int t = 0; t < total; t++) {
            int i = s.nextInt();
            String input = s.next();
            String output = "";
            for (int j = 0; j < input.length(); j++) {
                for (int k = 0; k < i; k++) {
                    System.out.print(input.charAt(j));
                }
            }
            System.out.println();
        }
    }
}
