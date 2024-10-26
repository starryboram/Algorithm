import java.io.*;
import java.util.*;

class Solution {
    public int[] solution(String my_string) {
        Map<String, Integer> map = new LinkedHashMap<>();
        for(int i = 65; i <= 90; i++) {
            map.put(String.valueOf((char)i), 0);
        }
        for(int j = 97; j <= 122 ; j++) {
            map.put(String.valueOf((char)j), 0);
        }

        for (int i = 0; i < my_string.length(); i++) {
            String s = String.valueOf(my_string.charAt(i));
            if (map.containsKey(s)) {
                map.put(s, map.get(s) + 1);
            }
        }

        Collection<Integer> valuesList = map.values();
        return valuesList.stream().mapToInt(Integer::intValue).toArray();
    }
}