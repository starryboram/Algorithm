public class 덧칠하기_17 {
    public static void main(String[] args) {
        int n = 8;
        int m = 4;
        int[] section = new int[]{2, 3, 6};
        solution(n, m, section);
    }

    public static int solution(int n, int m, int[] section) {
        int answer = 0;

        int[] arr = new int[n+1];
        for (int i = 0 ; i < section.length ; i++) {
            int value = section[i];
            arr[value] = - 1;
        }

        int idx = section[0];
        while (idx < arr.length) {
            if(arr[idx] == -1) {
                int settingIdx = idx + m > arr.length ? arr.length : idx + m;

                for(int i = idx ; i < settingIdx ; i++) {
                    arr[i] = 0;
                }
                idx += m;
                answer ++;
            } else {
                idx++;
            }
        }
        return answer;
    }

}