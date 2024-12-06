class solution {
    public static String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        int a = 0;
        int b = 0;

        int i = 0;
        while (i < goal.length){
            if(a < cards1.length && goal[i].equals(cards1[a])) {
                a++;
            } else if(b < cards2.length && goal[i].equals(cards2[b])){
                b++;
            } else {
                answer = "No";
                break;
            }
            i++;
        }
        return answer;
    }
}
