import java.util.*;
import java.lang.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> list = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();
        
        for (int i=0; i<progresses.length; i++){
            q.offer((int)Math.ceil((100.0-progresses[i]) / speeds[i]));
        }
        System.out.println(q);
        
        int now = q.poll();
        int cnt = 1;
        while(!q.isEmpty()){
            if (now >= q.peek()){
                cnt++;
                q.poll();
            }else{
                list.add(cnt);
                cnt = 1;
                now = q.poll();
            }
        }
        list.add(cnt);
        
        // ArrayList -> int []
        int[] answer = new int[list.size()];
        for(int i=0; i<answer.length;i++){
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}