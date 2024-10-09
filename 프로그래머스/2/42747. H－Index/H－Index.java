import java.util.*;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        
        for (int i=citations[citations.length-1]; i>=0; i--){
            // i의 위치 찾기
            int cnt = 0;
            for (int j=0; j<citations.length; j++){
                if(citations[j] < i){
                    continue;
                }
                cnt = citations.length - j;
                break;
            }
            
            if (cnt >= i){
                return i;
            }
            
        }
        return 0;
    }
}