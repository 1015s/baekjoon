import java.util.*;
import java.lang.*;

// 던전을 최대한 많이 탐험
class Solution {
    static boolean[] visited;
    static int answer = 0;
    
    private void dfs(int n, int hp, int[][] dungeons){
        for(int i=0; i<dungeons.length; i++){
            if (visited[i]) continue;
            if (hp >=dungeons[i][0]){
                visited[i] = true;
                dfs(n+1, hp-dungeons[i][1], dungeons);
                visited[i] = false;
            }
        }
        answer = Math.max(answer, n);
    }
    
    public int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];  
        dfs(0, k, dungeons);
        return answer;
    }
}