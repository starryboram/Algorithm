class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        for (int i = 0 ; i < num_list.length; i++){
            if(num_list[i] >= 0) {
                answer += 1;
            } else {
                break;
            }
        }
        if (answer == num_list.length) {
            return -1;
        }

        return answer;
    }
}

class Solution {
    public int solution(int[] num_list) {
        for (int i = 0;i < num_list.length;i++)
            if (num_list[i] < 0)
                return i;
        return -1;
    }
}

class Solution {

    public int solution(int[] num_list) {
        int answer = 0;
        for (num : num_list){
            if (num<0) {
                break;
            }
            answer ++;
        }
        return (answer == num_list.length) ? -1 : answer;
    }
}

class Solution {
    public int solution(int[] num_list){
        return IntStream.range(0, num_list.length)
                .filter(i -> num_listg[i] < 0)
                .findFirst()
                .orElse(-1);
    }
}