import java.util.*;

// 첫번쨰 풀이 - 틀린 이유 (두자리 수인 경우 -> 원하는 결과를 얻지 못한다.)
class Solution {
    public int[] solution(int[] arr) {
        String str = "";
        for (int i = 0; i < arr.length; i++) {
            String s = String.valueOf(arr[i]);
            str += s.repeat(arr[i]);
        }

        int[] answer = new int[str.length()];
        String[] arrays = str.split("");
        for (int i = 0; i < str.length(); i++) {
            answer[i] = Integer.parseInt(arrays[i]);
        }
        return answer;

    }

    // 정석대로 풀기로 했다.
    public int[] solution2(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int a : arr) {
            int cnt = a;
            while (cnt > 0) {
                list.add(a);
                cnt--;
            }
        }
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}