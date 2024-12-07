import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        List<Integer> list = Arrays.stream(arr).boxed().collect(Collectors.toList());
        Set<Integer> deleteSet = Arrays.stream(delete_list).boxed().collect(Collectors.toSet());

        list.removeIf(deleteSet::contains);
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}