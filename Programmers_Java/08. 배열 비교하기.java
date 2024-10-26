class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int arr1len = arr1.length;
        int arr2len = arr2.length;
        if (arr1len > arr2len) {
            return 1;
        } else if (arr1len < arr2len) {
            return -1;
        } else {
            int sum1 = 0, sum2 = 0;
            for (int a : arr1) {
                sum1 += a;
            }
            for (int aa : arr2) {
                sum2 += aa;
            }
            return resultSum(sum1, sum2);
        }
    }

    public int resultSum(int sum1, int sum2) {
        if(sum1 > sum2) return 1;
        else if(sum1 < sum2) return -1;
        else return 0;
    }
}

// 다른사람 풀이
class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int answer = Integer.compare(arr1.length, arr2.length);

        if(answer == 0) {
            answer = Integer.compare(IntStream.of(arr1).sum(), IntStream.of(arr2).sum());
        }

        return answer;
    }
}