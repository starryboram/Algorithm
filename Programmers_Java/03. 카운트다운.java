// 정수 start_num와 end_num가 주어질 때, start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
class Solution {
    public int[] solution(int start_num, int end_num) {
        int[] answer = new int[start_num - end_num + 1];
        for (int i = 0; i <= start_num - end_num; i++) {
            answer[i] = start_num - i;
        }
        return answer;
    }
}

class Solution {
    public int[] solution(int start, int end) {
        return IntStream
                .rangeClosed(-start, -end)
                .map(i -> -i)
                .toArray();
    }
}
