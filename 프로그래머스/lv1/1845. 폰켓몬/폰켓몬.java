import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        Map pon=new HashMap();
        for(int i=0; i<nums.length; i++){
            if(pon.containsKey(nums[i])){
                pon.put(nums[i],(int) pon.get(nums[i])+1);
            }else{
                pon.put(nums[i],1);
            }
        }
        System.out.println(pon);
        if (pon.size()>=nums.length/2){
            answer=nums.length/2;
        }else{
            answer=pon.size();
        }      
        return answer;
    }
}