import java.util.*;

// 네트워크 개수 - bfs
class Solution {
    private Set<Integer> bfs(int n, int[][] computers){
        Queue<Integer> q = new LinkedList<>();
        Set<Integer> set = new HashSet<>();
        
        q.offer(n);
        
        // bfs
        boolean[] visited = new boolean[computers.length];
        while(!q.isEmpty()){
            int cur = q.poll();
            
            if (visited[cur]) continue;
            visited[cur] = true;
            set.add(cur);
            
            for(int i=0; i<computers.length; i++){
                if (!visited[i] && computers[cur][i] == 1){
                    q.offer(i);
                }
            }
        }
        
        return set;
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        Set<Integer> mergedSet = new HashSet<>();
        
        for(int i=0; i<n; i++){
            if(mergedSet.contains(i)) continue;
            mergedSet.addAll(bfs(i, computers));
            answer++;
        }
        
        return answer;
    }
}