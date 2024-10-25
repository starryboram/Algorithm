import java.util.*;
import java.io.*;
import java.lang.*;

class Main {

    public static String FirstReverse(String str) {
        // code goes here
        StringBuilder sb = new StringBuilder(str);
        return sb.reverse().toString();
    }

    public static void main (String[] args) {
        // keep this function call here
        Scanner s = new Scanner(System.in);
        System.out.print(FirstReverse(s.nextLine()));
    }

}