import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer=new StringTokenizer(bufferedReader.readLine());
        int n=Integer.parseInt(stringTokenizer.nextToken());
        int k=Integer.parseInt(stringTokenizer.nextToken());

        int[] times=new int[100001];
        int[] visited=new int[100001];

        ArrayList queue=new ArrayList();
        queue.add(n);
//        ArrayList visited=new ArrayList();
        visited[n]=1;
        while (!queue.isEmpty()){
            int node=(int)queue.get(0);
            queue.remove(0);
//            System.out.println("node = " + node);

            if(node==k){
                System.out.println(times[node]);
                break;
            }

            if(0<=node-1 && node-1<=100000 && visited[node-1]!=1){
                visited[node-1]=1;
                queue.add(node-1);
                times[node-1]=times[node]+1;
            }
            if(0<=node+1 && node+1<=100000 && visited[node+1]!=1){
                visited[node+1]=1;
                queue.add(node+1);
                times[node+1]=times[node]+1;
            }
            if(0<=node*2 && node*2<=100000 && visited[node*2]!=1){
                visited[node*2]=1;
                queue.add(node*2);
                times[node*2]=times[node]+1;
            }
        }
    }
}
