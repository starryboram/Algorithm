import java.util.*;
import java.io.*;

class Main {

    public static int BracketCombinations(int num) {
        int [] arr = new int[num+2];
        arr[1] = 1;
        arr[2] = 2;
        arr[3] = 5;

        if (num >= 4) {
            for (int i = 4 ; i <= num; i++ ){
                arr[i] = 3 * arr[i-1] - 1;
            }
        }
        return arr[num];
    }

    public static void main (String[] args) {
        // keep this function call here
        Scanner s = new Scanner(System.in);
        System.out.print(BracketCombinations(s.nextLine()));
    }

}