import java.util.*;

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        
        Arrays.sort(d);
        for (int i=0; i<d.length; i++){
            int dept=(int) d[i];
            
            if(budget-dept>=0){
                // System.out.println(budget);
                // System.out.println(dept);
                budget=budget-dept;
                answer+=1;
            }else{
                break;
            }
        }
        
        
        return answer;
    }
}