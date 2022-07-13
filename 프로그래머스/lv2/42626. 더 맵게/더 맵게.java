import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;   
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for(int s:scoville){
            minHeap.add(s);
        }
        // System.out.println(minHeap);
        
        while(minHeap.size()>=2){
            int n1=minHeap.poll();
            int n2=minHeap.poll();
            
            if(n1>K){
                break;
            }else{
                minHeap.add(n1+n2*2);
                answer=answer+1;
            }
        }
        
        if(minHeap.size()!=0 && minHeap.poll()<K){
            answer=-1;
        }
            
        return answer;
    }
}