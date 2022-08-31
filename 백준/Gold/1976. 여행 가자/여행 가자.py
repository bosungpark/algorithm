import sys

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

graph=list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
plan=list(map(int, sys.stdin.readline().split()))
parents=list(i for i in range(n))

def find(x):
    if parents[x]!=x:
        return find(parents[x])
    return parents[x]

def union(x,y):
    x=find(x)
    y=find(y)
    
    if x<y:
        parents[y]=x
    else:
        parents[x]=y

def solver():
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                union(i,j) 
         
    answer=set()
    for p in plan:
        answer.add(find(parents[p-1]))
    if len(answer)==1:
        return print("YES")
    return print("NO")  
solver()