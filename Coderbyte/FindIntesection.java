import java.util.*;
import java.io.*;

class Main {

    public static String FindIntersection(String[] strArr) {
        String[] strArr1 = strArr[0].split(", ");
        String[] strArr2 = strArr[1].split(", ");

        int i = 0, j = 0;
        StringBuilder result = new StringBuilder();

        while(i<strArr1.length && j<strArr2.length) {
            int num1 = Integer.parseInt(strArr1[i]);
            int num2 = Integer.parseInt(strArr2[j]);

            if(num1 == num2) {
                if(result.length() > 0) result.append(",");
                result.append(num1);
                i++;
                j++;
            } else if (num1 > num2) {
                j++;
            } else {
                i++;
            }

        }

        return result.length() > 0 ? result.toString() : "false";
    }

    public static void main (String[] args) {
        // keep this function call here
        Scanner s = new Scanner(System.in);
        System.out.print(FindIntersection(s.nextLine()));
    }

}