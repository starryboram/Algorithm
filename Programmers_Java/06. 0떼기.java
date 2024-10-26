class Solution {
    public String solution(String n_str) {

        int firstNonZero = 0;
        while (firstNonZero < n_str.length() && n_str.charAt(firstNonZero) == '0') {
            firstNonZero++;
        }

        return n_str.substring(firstNonZero);
    }
}

// 다른사람 풀이
class Solution {
    public String solution(String n_str) {
        return ""+Integer.parseInt(n_str);
    }
}