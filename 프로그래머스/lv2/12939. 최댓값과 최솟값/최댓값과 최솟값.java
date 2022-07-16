class Solution {
    public String solution(String s) {
        String answer = "";
        
        int maximum=-10000000;
        int minimum=10000000;
        
        String temp="";
        s=s+" ";
        for(int i=0; i<s.length(); i++){
            
            
            if(s.charAt(i)==' '){
                // System.out.println(temp);
                int compare=Integer.parseInt(temp);
                // System.out.println(compare);
                if(compare>maximum){
                    maximum=compare;
                }
                if(compare<minimum){
                    minimum=compare;
                }
                
                temp="";
            }else{
                temp=temp + Character.toString(s.charAt(i));
            }
        }
        
        // System.out.println(maximum);
        // System.out.println(minimum);
        answer=minimum+" "+maximum;
        return answer;
    }
}