import java.util.*;

// 바로 앞 번호의 학생이나 바로 뒷 번호의 학생에게만 빌려줄 수 있음
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n;
        Map<Integer, Integer> map = new HashMap<>();
        
        Arrays.sort(lost);
        Arrays.sort(reserve);
        
        for(int i=0; i<reserve.length; i++){
            map.put(reserve[i], 2);
        }
        
        // 도난 = 여벌
        for(int i=0; i<lost.length; i++){
            int lost_person = lost[i];
            if(map.containsKey(lost_person)){
                map.remove(lost_person);
                lost[i] = -1;
            }
        }
        
        // 도난 != 여벌
        for(int i=0; i<lost.length; i++){
            if (lost[i] == -1) continue;
            if (map.containsKey(lost[i]-1) && map.get(lost[i]-1) > 1) {
                map.put(lost[i]-1, 1);
                
            }else if (map.containsKey(lost[i]+1) && map.get(lost[i]+1) > 1){
                map.put(lost[i]+1, 1);
            }else{
                answer -= 1;
            }
            
        }
        
        return answer;
    }
}