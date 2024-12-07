import java.util.*;
import java.io.*;

class Solution {
    public int[][] solution(int[][] arr) {
        int row = arr.length;
        int column = arr[0].length;
        int length = Math.max(row, column);

        int[][] answer = new int[length][length];

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                answer[i][j] = arr[i][j]; // 기본 배열은 0으로 초기화
            }
        }
        return answer;
    }
}