class Solution {
    public int[] solution(int[] arr) {
        int n = arr.length;
        int power = 1;
        while (power < n) {
            power *= 2;
        }
        int[] result = new int[power];
        System.arraycopy(arr, 0, result, 0, n);
        return result;
    }
}