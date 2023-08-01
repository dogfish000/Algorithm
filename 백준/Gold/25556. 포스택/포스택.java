import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());
        int[] arrInt = new int[n];
        String str = sc.nextLine();
        String[] arrStr = str.split(" ");

        String answer = "YES";

        for (int i = 0; i < n; i++) {
            arrInt[i] = Integer.parseInt(arrStr[i]);
        }

        int[] stack = new int[4];

        for (int i = 0; i < n; i++) {
            if (arrInt[i] >= stack[0]) {
                stack[0] = arrInt[i];
            } else if (arrInt[i] >= stack[1]) {
                stack[1] = arrInt[i];
            } else if (arrInt[i] >= stack[2]) {
                stack[2] = arrInt[i];
            } else if (arrInt[i] >= stack[3]) {
                stack[3] = arrInt[i];
            } else {
                answer = "NO";
                break;
            }
        }

        System.out.println(answer);


    }
}
