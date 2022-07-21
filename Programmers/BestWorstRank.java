public class BestWorstRank {
    class Solution {
        public int[] solution(int[] lottos, int[] win_nums) {
            int cnt= 0, zc=0;
            
            for(int i: lottos){
                if(i==0) {
                    zc++;
                    continue;
                }
                for(int j: win_nums){
                    if(i==j) {
                        cnt++;
                        break;
                    }
                }
            }
            int max = cnt+zc >= 2 ? 7-(cnt+zc) : 6;
            int min = cnt >= 2 ? 7-cnt : 6;
            int[] answer = {max, min};
            return answer;
        }
    }
}
