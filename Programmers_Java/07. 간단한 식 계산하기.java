class Solution {
    public int solution(String binomial) {
        String[] arr = binomial.split(" ");
        int a = Integer.parseInt(arr[0]);
        String s = arr[1];
        int b = Integer.parseInt(arr[2]);

        if(s.equals("+")) return a+b;
        else if (s.equals("-")) return a-b;
        else return a*b;
    }
}