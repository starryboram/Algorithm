import java.util.*;
import java.io.*;

class Main {

    public static String LongestWord(String sen) {
        String[] words = sen.replaceAll("[^a-zA-Z0-9 ]", "").split("\\s+");
        String longest = "";
        for (String word : words) {
            if (word.length() > longest.length()) {
                longest = word;
            }
        }
        return longest;
    }

    public static void main (String[] args) {
        // keep this function call here
        Scanner s = new Scanner(System.in);
        System.out.print(LongestWord(s.nextLine()));
    }
