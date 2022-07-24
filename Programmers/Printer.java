import java.util.*;
public class Printer {
    public int solution(int[] priorities, int location) {
        Queue<Integer> q = new LinkedList<>();
        Queue<Integer> aq = new LinkedList<>();
        int answer = 0, idx=0;
        for(int i : priorities){
            q.offer(i);
            aq.offer(idx);
            idx++;
        } 
        while (true){
            int max=0;
            for(int i : q) max=Math.max(i, max);
            if(q.peek()==max){
                q.poll();
                answer++;
                if(aq.poll()==location) break;
            }
            else{
                q.add(q.poll());
                aq.add(aq.poll());
            }
        }
        return answer;
    }
}
