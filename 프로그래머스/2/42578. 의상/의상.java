import java.util.*;

// 서로 다른 옷의 조합의 수
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        // HashMap 사용
        Map<String, Integer> map = new HashMap<>();
        
        for (int i=0; i<clothes.length; i++){
            map.put(clothes[i][1], map.getOrDefault(clothes[i][1], 0) + 1); // 안 입는 경우 고려
        }
        
        for(String key : map.keySet()){
            answer *= (map.get(key) + 1);
        }
        
        answer -= 1;
        
        return answer;
    }
}