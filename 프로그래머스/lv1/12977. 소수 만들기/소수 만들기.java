import java.util.*;

class Solution {
    
    public boolean isPrime(int n){
        if(n==1){
            return false;
        }
        for(int i=2; i<n; i++){
            if(n%i==0){
                return false;
            }
        }
        return true;
    }
    ArrayList comb=new ArrayList();
    
    public void combi(int[] nums,ArrayList visited){
             
        if(visited.size()==3){
            ArrayList copyed=(ArrayList) visited.clone();
            Collections.sort(copyed);
            comb.add(copyed);
            return;
        }
        for(int n:nums){
            // System.out.println(visited.contains(n));
            // System.out.println(visited);
            // System.out.println(n);
            if(!visited.contains(n)){
                visited.add(n);
                combi(nums,visited);
                visited.remove(visited.size()-1);
            }
        }
        return;
    }
    
    public int solution(int[] nums) {
        int answer = 0;
        int s=0;

        combi(nums, new ArrayList());
        Set co=new HashSet(comb);
        // System.out.println(comb);
        for(Object c: co){
            // System.out.println(c);
            
            for(Object i : (ArrayList) c){
                s=s+(int) i;
            }
            // System.out.println(s);
            if(isPrime(s)){
                // System.out.println(s);
                answer=answer+1;
            }
            s=0;
        }

        return answer;
    }
}