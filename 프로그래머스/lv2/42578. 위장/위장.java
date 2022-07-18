import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map choices=new HashMap();
        for(String[] c:clothes){
            String item=c[0];
            String category=c[1];
            
            if(choices.containsKey(category)){
                ArrayList a=(ArrayList)choices.get(category);
                a.add(item);
                choices.put(category,a);
            }else{
                ArrayList a=new ArrayList();
                a.add(item);
                choices.put(category,a);
            }
            
        }
        // System.out.println(choices);
        int answer=1;
        for(Object key : choices.keySet()){
            ArrayList value=(ArrayList)choices.get((String)key);
            answer=answer*(value.size()+1);
        }
        return answer-1;
    }
}