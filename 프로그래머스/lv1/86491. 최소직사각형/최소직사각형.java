class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        int bigger_max=0;
        int smaller_max=0;
        
        for(int[] s:sizes){
            int bigger=Math.max(s[0],s[1]);
            int smaller=Math.min(s[0],s[1]);
            
            bigger_max=Math.max(bigger_max,bigger);
            smaller_max=Math.max(smaller_max,smaller);
        }
        
        answer=bigger_max*smaller_max;
        return answer;
    }
}