public class 지폐접기_18 {
    public static void main(String[] args) {
        int[] wallet = new int[]{30, 15};
        int[] bill = new int[]{27, 17};
        solution(wallet, bill);
    }

    public static int solution(int[] wallet, int[] bill) {
        int answer = 0;
        int walletMinValue = Math.min(wallet[0], wallet[1]);
        int walletMaxValue = Math.max(wallet[0], wallet[1]);
        int billMinValue = Math.min(bill[0], bill[1]);
        int billMaxValue = Math.max(bill[0], bill[1]);

        while (true) {
            if(walletMinValue >= billMinValue && walletMaxValue >= billMaxValue) {
                break;
            }

            int halfBillValue = billMaxValue/2;
            billMaxValue = Math.max(halfBillValue, billMinValue);
            billMinValue = Math.min(halfBillValue, billMinValue);
            answer ++;
        }
        return answer;
    }

}