import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map completions=new HashMap();
        for(String c : completion){
            if(!completions.containsKey(c)){
                completions.put(c,1);
            }else{
                // System.out.println(c);
                completions.put(c,(int) completions.get(c)+1);
            }
            
        }
        
        for(String p: participant){
            if(!completions.containsKey(p)){
                return p;
            }else{
                completions.put(p,(int) completions.get(p)-1);
            }
        }
        // System.out.println(completions);
        for(String p: participant){
            if(completions.containsKey(p) && (int)completions.get(p)<0){
                return p;
            }
        }
        return answer;
    }
}