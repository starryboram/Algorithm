import java.util.*;
import java.io.*;

class Main {

    public static int FirstFactorial(int num) {
        return num == 1 ? 1 : num * FirstFactorial(num -1);
    }

    public static void main (String[] args) {
        // keep this function call here
        Scanner s = new Scanner(System.in);
        System.out.print(FirstFactorial(s.nextLine()));
    }

}