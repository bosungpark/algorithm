class Solution {
    public int solution(int n) {
        int answer = 0;
        int sum;  
        
        for(int i=1; i<=n; i++){
            sum=i;
            for(int j=i+1; j<=n+1; j++){
                if(sum>n){
                    break;
                }
                // System.out.println(sum);
                if(sum==n){
                    answer=answer+1;
                    break;
                }
                sum=sum+j;
            }
        }
        return answer;
    }
}