import java.util.*;
import java.io.*;

class Main {

    public static String BracketMatcher(String str) {
        Queue<String> q = new LinkedList<>();
        for (int i = 0 ; i < str.length(); i++) {
            if (str.charAt(i) == '(') {
                q.add("(");
            } else if (str.charAt(i) == ')') {
                if(q.isEmpty()) {
                    return "0";
                }
                q.poll();
            }
        }
        return (q.isEmpty()) ? "1" : "0";
    }

    public static void main (String[] args) {
        // keep this function call here
        Scanner s = new Scanner(System.in);
        System.out.print(BracketMatcher(s.nextLine()));
    }
}