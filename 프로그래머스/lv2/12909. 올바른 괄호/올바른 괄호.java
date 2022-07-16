import java.util.*;

class Solution {
    boolean solution(String s) {
        
        ArrayList stack=new ArrayList();
        
        for(int i=0; i<s.length(); i++){
            // System.out.println(stack);
            char b= s.charAt(i);
            if(b=='('){
                stack.add(b);
            }else{
                if(stack.size()!=0 && (char) stack.get(stack.size()-1)=='('){
                    stack.remove(stack.size()-1);
                }else{
                    return false;
                }
            }
        }
        
        if (stack.size()!=0){
            return false;
        }
        return true;
    }
}