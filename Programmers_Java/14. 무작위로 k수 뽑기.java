import java.util.*;
import java.io.*;

class Solution {
    public int[] solution(int[] arr, int k) {
        int[] answer = new int[k];
        Set<Integer> set = new LinkedHashSet<>();

        for (int num : arr) {
            set.add(num);
        }

        List<Integer> list = new ArrayList<>(set);

        for (int i = 0; i < k; i++) {
            if (i < list.size()) {
                answer[i] = list.get(i);
            } else {
                answer[i] = -1;
            }
        }
        return answer;
    }
}

