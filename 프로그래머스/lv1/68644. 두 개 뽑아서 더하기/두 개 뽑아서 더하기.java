import java.util.*;
class Solution {
    public ArrayList solution(int[] numbers) {
        Set answer = new HashSet();
        
        for(int i=0; i<numbers.length; i++){
            for(int j=i+1; j<numbers.length; j++){
                answer.add(numbers[i]+numbers[j]);
            }
        }
        // System.out.println(answer);
        ArrayList final_asnwer= new ArrayList(answer);
        Collections.sort(final_asnwer);
        return final_asnwer;
    }
}