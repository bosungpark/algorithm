import java.util.*;

class Solution {
    public ArrayList solution(int[] answers) {
        ArrayList answer = new ArrayList();
        
        int[] p1={1, 2, 3, 4, 5};
        int[] p2={2, 1, 2, 3, 2, 4, 2, 5};
        int[] p3={3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int cnt1=0;
        int cnt2=0;
        int cnt3=0;
        
        for(int i=0; i<answers.length; i++){
            if(answers[i]==p1[i%(p1.length)]){
                cnt1=cnt1+1;
            }
            if(answers[i]==p2[i%(p2.length)]){
                cnt2=cnt2+1;
            }
            if(answers[i]==p3[i%(p3.length)]){
                cnt3=cnt3+1;
            }
        }
        
        int maximum=0;
        maximum=Math.max(maximum,cnt1);
        maximum=Math.max(maximum,cnt2);
        maximum=Math.max(maximum,cnt3);
            
        if(cnt1==maximum){
            answer.add(1);
        }
        if(cnt2==maximum){
            answer.add(2);
        }
        if(cnt3==maximum){
            answer.add(3);
        }
          
        return answer;
    }
}