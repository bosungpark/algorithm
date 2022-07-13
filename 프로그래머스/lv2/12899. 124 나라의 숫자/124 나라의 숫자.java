class Solution {
    public String solution(int n) {
        String answer = "";
        while(n!=0){
            if(n%3!=0){
                answer+=Integer.toString(n%3);
                n=n/3;
            }else{
                answer+="4";
                n=n/3-1;
            }
        }
        
        StringBuffer sb=new StringBuffer(answer);  
        return sb.reverse().toString();
    }
}