import java.util.LinkedList;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int count = 0;
//        sc.nextLine();

        LinkedList<Integer> deque = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            deque.add(i);
        }

        int[] remove = new int[m];

        for (int i = 0; i < m; i++) {
            remove[i] = sc.nextInt();
        }
        sc.nextLine();


        for (int i = 0; i < m; i++) {
            int targetIdx = deque.indexOf(remove[i]);
            int halfIdx;

            if (deque.size() % 2 == 0) {
                halfIdx = deque.size() / 2 - 1;
            } else {
                halfIdx = deque.size() / 2;
            }

            if (targetIdx <= halfIdx) {
                for (int j = 0; j < targetIdx; j++) {
                    int temp = deque.removeFirst();
                    deque.addLast(temp);
                    count++;
                }
            } else {
                for (int j = deque.size() - 1; j >= targetIdx ; j--) {
                    int temp = deque.removeLast();
                    deque.addFirst(temp);
                    count++;
                }
            }
            deque.removeFirst();

        }

        System.out.println(count);


    }
}
