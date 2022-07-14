class Solution {
    public String solution(int a, int b) {
        String answer = "";
        int date=0;
        
        int month=1;
        while(month<a){
            if(month==1){
                date=date+31;
            }else if(month==2){
                date=date+29;
            }else if(month==3){
                date=date+31;
            }else if(month==4){
                date=date+30;
            }else if(month==5){
                date=date+31;
            }else if(month==6){
                date=date+30;
            }else if(month==7){
                date=date+31;
            }else if(month==8){
                date=date+31;
            }else if(month==9){
                date=date+30;
            }else if(month==10){
                date=date+31;
            }else if(month==11){
                date=date+30;
            }else if(month==12){
                date=date+31;
            }
            month++;
        }
        // System.out.println(date);
        date=date+b-1;
        
        System.out.println(date%7);
        if(date%7==1){
            answer="SAT";
        } else if(date%7==2){
            answer="SUN";
        }else if(date%7==3){
            answer="MON";
        }else if(date%7==4){
            answer="TUE";
        }else if(date%7==5){
            answer="WED";
        }else if(date%7==6){
            answer="THU";
        }else if(date%7==0){
            answer="FRI";
        }
        
        
        
        return answer;
    }
}