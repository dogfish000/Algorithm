
import java.util.Arrays;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.nextLine();

        String[] answer = new String[str.length()];

        for (int i = 0; i < str.length(); i++) {
            answer[i] = str.substring(i);
        }

        Arrays.sort(answer);

        for (int i = 0; i < answer.length; i++) {
            System.out.println(answer[i]);
        }

    }
}
