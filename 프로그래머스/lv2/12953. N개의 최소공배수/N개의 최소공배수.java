import java.util.*;

class Solution {
    public int solution(int[] arr) {
        int answer = 1;
        Map set=new HashMap();
        
        for(int a:arr){
            // System.out.println(a);
            int d=2;
            int cnt=0;
            
            while(d<=a){
                
                // System.out.println(cnt);
                if(a%d==0){
                    cnt=cnt+1;
                    if (set.containsKey(d)){
                        if((int) set.get(d)<cnt){
                            set.put(d,cnt);
                        }
                    }else{
                        // System.out.println(d);
                        set.put(d,cnt);
                    } 
                    a=a/d;
                }else{           
                    cnt=0;
                    d++;
                }
            }
            // System.out.println();
        }
        // System.out.println(set);
        for(Object k : set.keySet()){
            answer=answer*(int)Math.pow((int) k,(int) set.get(k));
        }
        return answer;
    }
}