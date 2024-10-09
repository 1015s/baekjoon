import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        // hash map
        Map<String, Integer> map = new HashMap<>();
        
        // hash map에 넣기
        for (int i=0; i<phone_book.length; i++){
            map.put(phone_book[i], i);
        }
        
        // 모든 경우의 수 in으로 검사
        for (int i=0; i<phone_book.length; i++){
            for(int j=0; j<phone_book[i].length(); j++){
                if (map.containsKey(phone_book[i].substring(0, j))){
                    return false;
                }
            }
        }
        return true;
    }
}