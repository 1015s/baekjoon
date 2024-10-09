import java.util.*;

class Solution {
    static List<String> list;
    static String [] alps = {"A", "E", "I", "O", "U"};
    
    private void dfs(String str, int n){
        list.add(str);
        if (n == 5) return;
        for(int i=0; i<5; i++){
            dfs(str+alps[i], n+1);
        }
    }
    
    public int solution(String word) {
        int answer = 0;
        list = new ArrayList<>();
        dfs("", 0);
        int size = list.size();
        for (int i=0; i<size; i++){
            if (word.equals(list.get(i))){
                answer = i;
            }
        }
        return answer;
    }
}