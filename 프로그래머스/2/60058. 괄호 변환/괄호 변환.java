import java.util.*;

class Solution {
    private boolean is_correct(String s){
        int cnt = 0;
        
        for(int i=0; i<s.length(); i++){
            if (cnt < 0) return false;
            if(s.charAt(i) == '('){
                cnt++;
            }else{
                cnt--;
            }
        }
        return true;
    }
    
    private String simulation(String p){
        // 1
        if (p.equals("")) return "";
        
        // 2 - 최소 균형잡힌 괄호 문자열 분리
        int left = 0;
        int right = 0;
        for(int i=0; i<p.length(); i++){
            if (p.charAt(i) == '('){
                left++;
            }else{
                right ++;
            }
            
            if(left == right) break;
        }
        String u = p.substring(0, left+right);
        String v = p.substring(left+right, p.length());
        
        if(is_correct(u)){
            return u + simulation(v);
        }else{
            String temp = "(" + simulation(v) + ")";
            for(int i=1 ; i<u.length()-1; i++){
                if (u.charAt(i) == ')'){
                    temp += "(";
                }else{
                    temp += ")";
                }
            }
            return temp;
        }
    }
    
    public String solution(String p) {
        String answer = "";
        return simulation(p);
    }
}