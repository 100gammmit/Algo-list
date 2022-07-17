import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        ArrayList<Integer> arrList = new ArrayList<>();
        int[] spj1 = {1, 2, 3, 4, 5};
        int[] spj2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] spj3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int s1=0, s2=0, s3=0, idx=0;
        for(int i=0; i<answers.length; i++)
        {
            if (answers[i] == spj1[i%5]) s1++;
            if (answers[i] == spj2[i%8]) s2++;
            if (answers[i] == spj3[i%10]) s3++;
        }
        if (s1 >= s2 && s1 >= s3) arrList.add(1);
        if (s2 >= s1 && s2 >= s3) arrList.add(2);
        if (s3 >= s1 && s3 >= s2) arrList.add(3);
        int[] answer = new int[arrList.size()];
        for (int i = 0 ; i < arrList.size() ; i++) {
        answer[i] = arrList.get(i);
        }
        return answer;
    }
}